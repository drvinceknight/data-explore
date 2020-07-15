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

def categorical_handle(data):
    """
    Transforms categorical data into numerical, saves maping on a list.
    """
    indexs = []
    for name in data.columns:
        if "O" == data[name].dtype:
            new = pd.factorize(data[name])
            data[name] = new[0]
            indexs.append(new[1])
    return data, indexs

def collect_column(data):
    return data.columns

def place_columns(database,col):
    database.columns = col
    return database

def place_categorical(index,data,cat):
    line = data[cat].round()
    for i in range(len(index)):
        line = line.replace(i,index[i])
    data[cat] = line
    return data

def timestamp_handle(times):
    m = times.minute
    hh = times.hour*100
    dd = times.day*10000
    mm = times.month*1000000
    yyyy = times.year*10000000
    numtime = m + hh + dd + mm + yyyy
    return numtime
