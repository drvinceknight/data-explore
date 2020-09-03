import subprocess
import dataexplorer
import os

def test_help():
    exp_output=b"""Usage: __main__.py [OPTIONS]\n\n  read data and logs it\n
Options:
  --target TEXT   the file that you want to import
  --table TEXT    what table you are using
  --output TEXT   the file that you are saving as
  --convert TEXT  the file extention you like to convert to
  --help          Show this message and exit.\n"""
    currunt_output=subprocess.run(["python","-m","dataexplorer","--help"],capture_output=True)
    assert currunt_output.stdout == exp_output

def test_main_func():
    out=subprocess.run(["python","-m","dataexplorer","--target=flight.db","--table=readings","--output=test/testing"])
    assert out.returncode == 0
    assert os.path.isfile("test.log")
    assert os.stat('test.log').st_size > 0

def test_convert():
    out=subprocess.run(["python","-m","dataexplorer","--target=flight.db","--table=readings","--convert=csv"])
    assert out.returncode == 0
    assert os.stat('flight.csv').st_size > 0
    out=subprocess.run(["python","-m","dataexplorer","--target=flight.csv","--convert=json"])
    assert out.returncode == 0
    assert os.stat('flight.json').st_size > 0
    subprocess.call(['rm','flight.db'])
    out=subprocess.run(["python","-m","dataexplorer","--target=flight.json","--table=readings","--convert=db"])
    assert out.returncode == 0
    assert os.stat('flight.db').st_size > 0
