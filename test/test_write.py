import dataexplorer
import os


def test_make_log_file():
    set = dataexplorer.load_sql("flight.db", "readings")
    stats = dataexplorer.get_stats(set)
    dataexplorer.make_log_file(stats, "test")
    assert os.path.isfile("./test.log")
