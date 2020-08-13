import click
import sqlalchemy as sa
import pandas as pd
import logging


#@click.command()
#@click.option("--target", help="the file that you want to import")
#@click.option("--table", help="what table you are using")
#@click.option("--output", help="the file that you are saving as")

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
    logging.basicConfig(filename='test.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s: \n%(message)s')
    logging.info(data)

def main(target, table, output):
    """
    read data and logs it
    """
    data = load_sql(target,table)
    stats = get_stats(data)
    make_log_file(stats, output)
    

if __name__ == '__main__':
    main()
