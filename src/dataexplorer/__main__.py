import sqlalchemy as sa
import pandas as pd
import click

@click.command()
@click.option("---target", prompt="the file that you want to import")
@click.option("--table", help="what table you are using")
@click.option("--output", help="the file that you are saving as")



def load_sql(file, table):
    """
    Loads an SQL table
    """
    engine = sa.create_engine("sqlite:///" + file + ".db")
    connection = engine.connect()
    database = pd.read_sql(table, connection)
    return database


def save_sql(df, file, table):
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
    return [mean, std, maxi, mini, no_field, length]


def categorical_handle(data):
    """
    transforms categorical data into numerical, saves maping on a list.
    this calls timestamp_handle fuction
    """
    indexs = []
    for name in data.columns:
        if "O" == data[name].dtype:
            new = pd.factorize(data[name])
            data[name] = new[0]
            indexs.append(new[1])
        elif "<M8[ns]" == data[name].dtype:
            times = timestamp_handle(data[name])
            data[name] = times
            indexs.append(["time"])
        else:
            indexs.append(["#"])
    return data, indexs


def place_time(data, cat):
    """
    transform time from numerical back to ctime
    """
    line = data[cat]
    fulltime = []
    for l in line:
        print(l)
        fulltime.append(time.ctime(l))
    data[cat] = fulltime
    return data


def collect_column(data):
    """
    collects the column name
    """
    return data.columns


def place_columns(database, col):
    """
    insert column name to the dataset
    """
    database.columns = col
    return database


def place_categorical(index, data, cat):
    """
    categorize numerical values based on the index list
    """
    line = data[cat].round()
    for i in range(len(index)):
        try: main.sql
            line = line.replace(i, index[i])
        except IndexError:
            line = line.replace(i, None)
    data[cat] = line
    return data


def timestamp_handle(times):
    """
    covert time into numrical this can be revert be time.ctime()
    """
    numtime = []
    for t in times:
        numtime.append(t.timestamp())
    return numtime

def make_log_file(data,filename):
    """
    makes a log file
    """
    pass

def export_numeric(numeric):
    """
    export the numeric vertion of the database to be used in other code
    """
    pass

def main_read(target, table, output):
    """
    read data and logs it
    """
    data = read_sql(target,table)
    stats = get_stats(data)
    cloumn = collect_column(data)
    numeric,index_list = categorical_handle(data)
    make_log_file([stats,cloumn,index_list], output)
    export_numeric(numeric)

def main_write():
    """
    write data
    """
    pass

if __name__ == '__main__':
    main_read()
