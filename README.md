## A tool to capture information about the general structure of an sql database

### Installation

To install:

    $ git clone <git address>
    $ cd sql-explore
    $ python setup.py develop 


### Use:

Given a file `main.sql` after installation we can run the tool using:

    sql-explore --target main.sql --output main.log


The `main.log` file will contain all the information about `main.sql`.

### Options:
  --target TEXT  the file that you want to import
  --table TEXT   what table you are using
  --output TEXT  the file that you are saving as
  --help         Show this message and exit.


### Test

To test the basic functionality, after installing:

    python -m pip install pytest. # If pytest is not already installed
    python -m pytest
