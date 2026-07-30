import pandas as pd


def load_cement_database():

    return pd.read_csv("data/cement_database.csv")


def get_cement_data(cement_class):

    database = load_cement_database()

    row = database[database["Class"] == cement_class]

    return row.iloc[0]