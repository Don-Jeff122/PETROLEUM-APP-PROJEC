import pandas as pd
import streamlit as st

from modules.constants import EXCESS_WARNING_THRESHOLD, PPG_TO_KG_M3
from modules.database import (
    load_cement_database,
    get_cement_data,
    load_additives_database,
    get_additive_data,
)
from modules.cement import (
    calculate_annular_volume,
    calculate_cement_volume,
    calculate_spacer_volume,
    calculate_flush_volume,
    calculate_pump_time,
    calculate_plug_bumping_pressure,
    evaluate_temperature_rating,
    validate_inputs,
)
from views.ui_style import (
    page_header,
    section_title,
    results_table,
    begin_calculation,
    calculated_button,
)


def show():

    page_header(
        "construction",
        "Cement Design",
        "Size a primary cement job using the API cement class database.",
    )

    database = load_cement_database()
    additives_db = load_additives_database()

    with st.container(border=True):
        section_title("Step 1", "Select Cement Class")
        cement_class = st.selectbox(
            "Cement Class",
            database["Class"],
            label_visibility="collapsed",
        )

    cement = get_cement_data(cement_class)

    with st.container(border=True):
        section_title("Properties", f"{cement_class} Specifications")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Density", f"{cement['Density_ppg']} ppg")
        with col2:
            st.metric("Yield", f"{cement['Yield_m3_per_sack']} m³/sack")
        with col3:
            st.metric("Max Temperature", f"{cement['Max_Temperature_C']} °C")
        with col4:
            st.metric("Recommended Use", cement["Recommended_Use"])

    input_col, info_col = st.columns([1.2, 1], gap="large")

    with input_col:
        with st.container(border=True):
            section_title("Step 2", "Well Geometry & Conditions")

            hole_diameter = st.number_input(
                "Hole Diameter (in)",
                min_value=0.0,
                value=8.5,
            )
            casing_od = st.number_input(
                "Casing Outside Diameter (in)",
                min_value=0.0,
                value=5.5,
            )
            interval_length = st.number_input(
                "Cement Interval (m)",
                min_value=0.0,
                value=1000.0,
            )
            excess_percent = st.number_input(
                "Excess / Washout (%)",
                min_value=0.0,
                value=15.0,
                help="Typical excess is 10–25%. Values above 50% suggest severe washout.",
            )
            bottom_hole_temp = st.number_input(
                "Bottom-Hole Temperature (°C)",
                min_value=0.0,
                value=60.0,
                help="Compared against the cement class maximum temperature rating.",
            )
            spacer_length = st.number_input(
                "Spacer Length (m)",
                min_value=0.0,
                value=50.0,
            )
            flush_length = st.number_input(
                "Flush Length (m)",
                min_value=0.0,
                value=30.0,
            )
            pump_rate = st.number_input(
                "Pump Rate (L/min)",
                min_value=1.0,
                value=300.0,
            )

            calculate = calculated_button(
                "Calculate Cement Design", "cement_results", "calculate_cement"
            )

        with st.container(border=True):
            section_title("Step 3", "Cement Additives")
            selected_additives = st.multiselect(
                "Select Additives",
                additives_db["Additive_Name"].tolist(),
                help="Additives are applied per sack of cement.",
            )

    with info_col:
        with st.container(border=True):
            section_title("Guide", "Volume Calculation")
            st.markdown(
                """
                Annular volume is calculated from hole and casing
                diameters over the cement interval, with excess
                applied for hole irregularities.

                **Required sacks** = Volume ÷ Yield per sack

                **Spacer** = Annular volume × Spacer length

                **Pump time** = Volume ÷ Pump rate
                """
            )

    if calculate:
        begin_calculation("Calculating Cement Design…")

        yield_per_sack = cement["Yield_m3_per_sack"]

        valid, message = validate_inputs(
            hole_diameter,
            casing_od,
            interval_length,
            excess_percent,
            yield_per_sack,
        )

        if not valid:
            st.error(message)
            return

        volume = calculate_annular_volume(
            hole_diameter,
            casing_od,
            interval_length,
            excess_percent,
        )
        sacks = volume / yield_per_sack

        # split into lead and tail slurries
        lead_volume, tail_volume = calculate_cement_volume(volume)

        # spacer, flush and pump time
        spacer_volume = calculate_spacer_volume(hole_diameter, casing_od, spacer_length)
        flush_volume = calculate_flush_volume(hole_diameter, flush_length)
        pump_time = calculate_pump_time(volume, pump_rate)

        # plug bumping pressure from cement column hydrostatics
        cement_density = cement["Density_ppg"] * PPG_TO_KG_M3
        bump_pressure = calculate_plug_bumping_pressure(
            interval_length, cement_density
        )

        # temperature rating check (stress-test logic)
        temp_rating, temp_margin = evaluate_temperature_rating(
            cement["Max_Temperature_C"], bottom_hole_temp
        )

        # additive schedule
        additive_rows = []
        for name in selected_additives:
            additive = get_additive_data(name)
            if additive is None:
                continue
            dosage_kg = additive["Dosage_kg_per_sack"]
            total_mass = dosage_kg * sacks
            additive_rows.append(
                {
                    "Additive": name,
                    "Category": additive["Category"],
                    "Dosage (kg/sack)": dosage_kg,
                    "Total (kg)": total_mass,
                    "Concentration (kg/m³)": total_mass / volume if volume else 0.0,
                    "Effect": additive["Effect"],
                    "Max Temp (°C)": additive["Max_Temperature_C"],
                }
            )

        st.session_state["cement_results"] = {
            "Cement Class": cement_class,
            "Density (ppg)": cement["Density_ppg"],
            "Yield (m³/sack)": yield_per_sack,
            "Max Temp (°C)": cement["Max_Temperature_C"],
            "Bottom-Hole Temp (°C)": bottom_hole_temp,
            "Temperature Rating": temp_rating,
            "Slurry Volume": volume,
            "Required Cement": sacks,
            "Lead Volume": lead_volume,
            "Tail Volume": tail_volume,
            "Spacer Volume": spacer_volume,
            "Flush Volume": flush_volume,
            "Pump Time": pump_time,
            "Bumping Pressure (Pa)": bump_pressure,
            "Excess (%)": excess_percent,
            "Additives": additive_rows,
        }

        st.divider()
        section_title("Results", "Cement Job Summary")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Annular Volume", f"{volume:.2f} m³")
        with col2:
            st.metric("Required Cement", f"{sacks:.0f} sacks")
        with col3:
            st.metric("Spacer Volume", f"{spacer_volume:.2f} m³")
        with col4:
            st.metric("Pump Time", f"{pump_time:.1f} min")

        col5, col6, col7, col8 = st.columns(4)
        with col5:
            st.metric("Lead Volume", f"{lead_volume:.2f} m³")
        with col6:
            st.metric("Tail Volume", f"{tail_volume:.2f} m³")
        with col7:
            st.metric("Flush Volume", f"{flush_volume:.2f} m³")
        with col8:
            st.metric("Bumping Pressure", f"{bump_pressure/1_000_000:.2f} MPa")

        # ── Warning logic (viva stress-test) ──
        if temp_rating == "EXCEEDED":
            st.error(
                f"Bottom-hole temperature ({bottom_hole_temp:.0f} °C) EXCEEDS the "
                f"{cement_class} rating of {cement['Max_Temperature_C']:.0f} °C by "
                f"{-temp_margin:.0f} °C. Select a higher-rated cement class or "
                "add a thermal stabilizer."
            )
        elif temp_rating == "LIMIT":
            st.warning(
                f"Bottom-hole temperature ({bottom_hole_temp:.0f} °C) is within "
                f"{temp_margin:.0f} °C of the {cement_class} rating "
                f"({cement['Max_Temperature_C']:.0f} °C). Consider a thermal stabilizer."
            )
        else:
            st.success(
                f"Temperature rating OK — {bottom_hole_temp:.0f} °C is "
                f"{temp_margin:.0f} °C below the {cement_class} limit."
            )

        if excess_percent > EXCESS_WARNING_THRESHOLD:
            st.warning(
                f"Excess of {excess_percent:.0f}% is very high. This suggests severe "
                "borehole washout — verify hole caliper data before pumping."
            )

        for row in additive_rows:
            if bottom_hole_temp > row["Max Temp (°C)"]:
                st.warning(
                    f"Additive {row['Additive']} is rated to {row['Max Temp (°C)']:.0f} °C "
                    f"but bottom-hole temperature is {bottom_hole_temp:.0f} °C."
                )

        # additive schedule table
        if additive_rows:
            section_title("Additives", "Additive Schedule")
            st.dataframe(
                pd.DataFrame(additive_rows),
                width="stretch",
                hide_index=True,
            )

        with st.container(border=True):
            results_table(
                [
                    "Cement Class",
                    "Density",
                    "Yield",
                    "Maximum Temperature",
                    "Bottom-Hole Temperature",
                    "Temperature Rating",
                    "Hole Diameter",
                    "Casing Outside Diameter",
                    "Cement Interval",
                    "Excess / Washout",
                    "Annular Volume",
                    "Required Cement",
                    "Spacer Volume",
                    "Flush Volume",
                    "Pump Time",
                    "Bumping Pressure",
                ],
                [
                    cement_class,
                    f"{cement['Density_ppg']} ppg",
                    f"{yield_per_sack:.3f} m³/sack",
                    f"{cement['Max_Temperature_C']} °C",
                    f"{bottom_hole_temp:.1f} °C",
                    temp_rating,
                    f"{hole_diameter:.2f} in",
                    f"{casing_od:.2f} in",
                    f"{interval_length:.2f} m",
                    f"{excess_percent:.2f} %",
                    f"{volume:.2f} m³",
                    f"{sacks:.0f} sacks",
                    f"{spacer_volume:.2f} m³",
                    f"{flush_volume:.2f} m³",
                    f"{pump_time:.1f} min",
                    f"{bump_pressure/1_000_000:.2f} MPa",
                ],
            )

        st.success("Cement design completed successfully.")
