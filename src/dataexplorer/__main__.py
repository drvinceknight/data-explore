import sqlalchemy as sa
import pandas as pd

def load_sql(file, table):
    """
    Loads an SQL table
    """
    engine = sa.create_engine("sqlite:///" + file + ".db")
    connection = engine.connect()

def save_sql(file):
    """
    Saves the data to an SQL table 
    """
    engine = sa.create_engine("sqlite:///" + file + ".db")
