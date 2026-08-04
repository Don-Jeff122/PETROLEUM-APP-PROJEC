# PyMudCement-Optima

Drilling fluid and cementing engineering software for mud weight design, rheology analysis, hydraulics calculations, cementing design, plug design, and plug & abandonment operations.

> Final year project — PENG 258: Drilling Engineering 1.

## Features

### Drilling Fluids & Hydraulics Engine
- **Mud Weight Design** — Calculate required mud density, hydrostatic pressure, and the safe mud weight window between pore and fracture pressure
- **Rheology Analysis** — Analyse viscometer readings using the Bingham plastic model (PV, YP) with flow-curve plotting
- **Hydraulics** — Annular velocity, hole cleaning rating, annular pressure drop, and Equivalent Circulating Density (ECD)

### Cementing Engineering Module
- **Cement Design** — Size primary cement jobs with the API cement class database, lead/tail splits, spacer & flush volumes, pump time, and plug bumping pressure
- **Temperature Rating Checks** — Warns when bottom-hole temperature exceeds the cement class rating or additive rating (stress-test logic)
- **Cement Additives** — Select from the additive database with per-sack dosage, total mass, and concentration calculations
- **Plug Design** — Calculate cement plug volume, sack requirements, and depth placement

### Plug & Abandonment Module
- **Abandonment plugs** — Volume and sack requirements for abandonment cement plugs
- **Squeeze cementing** — Squeeze volume and sack calculations with user-defined efficiency
- **Balanced plug** — Column length and cement hydrostatic pressure at plug bottom

### Reporting
- **Results Dashboard** — Consolidated summary of all saved calculations with workflow progress
- **PDF Engineering Report** — Generic calculation report of all saved results
- **Cementing Job Procedure Sheet** — Formal one-page job procedure with slurry design, volumetric schedule, additive schedule, and sign-off blocks

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/PyMudCement-Optima.git
cd PyMudCement-Optima
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
streamlit run app.py
```

## Dependencies

- Python 3.10+
- Streamlit
- Pandas
- NumPy
- Plotly
- ReportLab

## Usage

1. Open the application in your browser
2. Select a module from the sidebar
3. Enter your well parameters
4. Click "Calculate" to see results
5. Export a PDF report or a cementing job procedure sheet from the Results page

## Project Structure

```
PyMudCement-Optima/
├── app.py                  # Main application entry point
├── requirements.txt        # Python dependencies
├── README.md               # This file
├── data/
│   ├── cement_database.csv # API cement classes (density, yield, temp rating)
│   └── additives.csv       # Cement additive database
├── modules/                # Calculation engine (no hardcoded values)
│   ├── constants.py        # Central engineering constants & conversions
│   ├── mud.py              # Mud weight calculations
│   ├── rheology.py         # Rheology calculations
│   ├── hydraulics.py       # Hydraulics calculations
│   ├── cement.py           # Cement calculations
│   ├── plug.py             # Plug design calculations
│   ├── abandonment.py      # Abandonment calculations
│   ├── database.py         # CSV database loading
│   └── report.py           # PDF report & job procedure generation
└── views/                  # Streamlit user interface
    ├── ui_style.py         # Global styling & shared UI helpers
    ├── mud_weight.py       # Mud weight view
    ├── rheology.py         # Rheology view
    ├── hydraulics.py       # Hydraulics view
    ├── cement_design.py    # Cement design view
    ├── plug_design.py      # Plug design view
    ├── abandonment.py      # Plug & abandonment view
    ├── results.py          # Results dashboard
    └── about.py            # About page
```

## Authors

Group ... — University of Energy and Natural Resources (UENR)

## License

This project is for educational purposes only.
