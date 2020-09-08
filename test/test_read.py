import dataexplorer
import pandas


def test_load_sql():
    df = dataexplorer.load_sql("flight.db", "readings")
    assert isinstance(df, pandas.DataFrame)


def test_get_stats():
    set = pandas.DataFrame(
        data={"a": [1, 2, 3], "b": [2, 3, 4], "c": ["com", "com", "sum"]}
    )
    stats = dataexplorer.get_stats(set)
    result = """         a    b
count  3.0  3.0
mean   2.0  3.0
std    1.0  1.0
min    1.0  2.0
25%    1.5  2.5
50%    2.0  3.0
75%    2.5  3.5
max    3.0  4.0"""
    assert str(stats) == result
