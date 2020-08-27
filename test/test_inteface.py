import subprocess
import dataexplorer
def test_help():
    exp_output=b"""Usage: __main__.py [OPTIONS]\n\n  read data and logs it\n
Options:
  --target TEXT  the file that you want to import
  --table TEXT   what table you are using
  --output TEXT  the file that you are saving as
  --help         Show this message and exit.\n"""
    currunt_output=subprocess.run(["python","-m","dataexplorer","--help"],capture_output=True)
    assert currunt_output.stdout == exp_output

def test_main_func():
    out=subprocess.run(["python","-m","dataexplorer","--target=flight","--table=readings","--output=test"])
    assert out.returncode == 0
#subprocess.run(["command","agument1,..."],catarer_output=True))
