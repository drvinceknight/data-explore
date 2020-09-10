import subprocess
import dataexplorer
import os
import pathlib
from randomdatagen import generate_random_testing_data


def test_help():
    exp_output = b"""Usage: __main__.py [OPTIONS]

  read data and logs it

Options:
  --target TEXT  the file that you want to import
  --table TEXT   what table you are using
  --output TEXT  the file that you are saving as
  --help         Show this message and exit.
"""
    current_output = subprocess.run(
        ["python", "-m", "dataexplorer", "--help"], capture_output=True
    )
    if os.name == 'nt':
        exp_output = exp_output.replace(b"\n",b"\r\n")
    assert current_output.stdout == exp_output


def test_main_func():
    if os.path.isfile("testing.log"):
        log_file = pathlib.Path("testing.log")
        log_file.unlink()
    if not os.path.isfile("flight.db"):
        generate_random_testing_data(20)
    out = subprocess.run(
        [
            "python",
            "-m",
            "dataexplorer",
            "--target=flight",
            "--table=readings",
            "--output=testing.log",
        ]
    )
    assert out.returncode == 0
    assert os.path.isfile("testing.log")
    assert os.stat("testing.log").st_size > 0
