import pandas as pd


def load_cement_database():
    return pd.read_csv("data/cement_database.csv")


def get_cement_data(cement_class):
    database = load_cement_database()
    row = database[database["Class"] == cement_class]
    return row.iloc[0]


def load_additives_database():
    return pd.read_csv("data/additives.csv")


def get_additive_data(additive_name):
    database = load_additives_database()
    row = database[database["Additive_Name"] == additive_name]
    if len(row) == 0:
        return None
    return row.iloc[0]