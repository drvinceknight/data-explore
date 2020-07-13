import sqlalchemy as sa
import pandas as pd

def load_sql(file, table):
    """
    Loads an SQL table and pre-procsses the table, ready to be trained
    """
    engine = sa.create_engine("sqlite:///" + file + ".db")
    connection = engine.connect()

def save_sql(file):
    """
    Saves the generated data to a SQL table called generated_data
    """
    engine = sa.create_engine("sqlite:///" + file + ".db")
