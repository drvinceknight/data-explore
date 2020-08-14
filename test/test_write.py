import dataexplorer
import os

def test_make_log_file():
    set = dataexplorer.load_sql('flight','readings')
    stats = dataexplorer.get_stats(set)
    dataexplorer.make_log_file(stats,'test')
    #assert os.path.exists('test.log')
