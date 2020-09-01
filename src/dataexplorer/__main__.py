import sqlalchemy as sa
import pandas as pd
import click
import logging

@click.command()
@click.option("--target", help="the file that you want to import")
@click.option("--table", help="what table you are using")
@click.option("--output", help="the file that you are saving as")
@click.option("--convert",help="the file extention you like to convert to",default=None)

def main(target, table, output,convert):
    """
    read data and logs it
    """
    name,extention = target.split('.')
    if extention == 'db':
        data = load_sql(name,table)
    elif extention == 'csv':
        data = pandas.read_csv(target)
    elif extention == 'json':
        data = pandas.read_json(target)
    elif extention == 'sav':
        data = pandas.read_spss(target)
    else:
        return None#raise Error("file type not supported")
    stats = get_stats(data)
    make_log_file(stats, output)
    if convert != None:
        save_file(data,convert,name)

def save_file(data,convert,name):
    if convert == 'db':
        save_sql(data,name,'table')
    elif convert == 'csv':
        pass
    elif convert == 'json':
        pass
    elif convert == 'sav':
        pass
    else:
        return None

def save_sql(df,file,table):
    """
    Saves the generated data to a SQL table called generated_data
    """
    engine = sa.create_engine("sqlite:///" + file + ".db")
    df.to_sql(table, con=engine, if_exists="append")

def load_sql(file, table):
    """
    Loads an SQL table
    """
    engine = sa.create_engine("sqlite:///" + file + ".db")
    connection = engine.connect()
    database = pd.read_sql(table, connection)
    return database

def get_stats(data):
    """
    provides the basic stats for the dataset
    """
    return data.describe()

def make_log_file(data,filename):
    """
    makes a log file
    """
    logging.basicConfig(filename=filename, level=logging.INFO,
                    format='%(asctime)s:%(levelname)s: \n%(message)s')
    logging.info(data)

if __name__ == '__main__':
    main()
