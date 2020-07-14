import sqlalchemy as sa
import pandas as pd

def load_sql(file, table):
    """
    Loads an SQL table 
    """
    engine = sa.create_engine("sqlite:///" + file + ".db")
    connection = engine.connect()
    database = pd.read_sql(table, connection)
    return database

def save_sql(df,file,table):
    """
    Saves the sql
    """
    engine = sa.create_engine("sqlite:///" + file + ".db")
    df.to_sql(table, con=engine, if_exists="append")
    
def get_stats(data):
    """
    provides the basic stats for the dataset
    """
    mean = data.mean()
    std = data.std()
    maxi = data.max()
    mini = data.min()
    no_field = len(data.columns)
    length = len(data)
    return [mean,std,maxi,mini,no_field,length]

