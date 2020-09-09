import dataexplorer
import os
from randomdatagen import generate_random_testing_data

def test_make_log_file():
    try:
        generate_random_testing_data(20)
    except Exception:
        pass
    set = dataexplorer.load_sql("flight", "readings")
    stats = dataexplorer.get_stats(set)
    dataexplorer.make_log_file(stats, "test")
    assert os.path.isfile("test.log")
