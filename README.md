## A tool to capture information about the general structure of tables within an sql database

The tool computes:
the number of records in a table of a given database (count), the mean value of all records in the table (mean) as well as their standard deviation (std), and their (0%, 25%, 50%, 75%, 100%) quartile

### Required softwares

To be able to install the software, it is necessary first to have a version of git (any version)
as well as a version of python 3.7 or 3.8 (this software has not been tested for further versions).
Also its is important that pip is installed.

### Virtual environment

If the tool needs to be run on an separate environment first, the following commands need to be run before the installation:

$ pip install venv

Then create the `<environment>` that the code will be run on :

$ python -m venv <environment>

Once the virtual environment is created, it needs to be activated with the following commands:

On Windows, run:

`<environment> \Scripts\activate.bat`

On Unix or MacOS, run:

source `<environment>`/bin/activate

### Installation

Open the terminal and enter the following commands:

    $ git clone https://github.com/Tompoudurans/data-explore
    $ cd data-explore
    $ python setup.py develop

### Utilisation

After installation,
For any `<table>` within a `<database>` sql file, the tool can be run entering the following command:
    $ data-explore --target=<database> --table=<table> --output=<log>

The `<log>` file  produced by this command will contain all the information about the general structure of the `<table>` held in <`database`>.

### Test

If the tool needs to be tested after installing, enter the following commands:

  $  python -m pip install pytest. # If pytest is not already installed
  $  python -m pytest
