## A tool to capture information about the general structure of tables within an sql database

The tool computes:
the number of records in a table of a given database (count), the mean value of all records in the table (mean) as well as their standard deviation (std), and their (0%, 25%, 50%, 75%, 100%) quartile

### Installation

To install, enter the following commands:

    $ git clone https://github.com/Tompoudurans/data-explore
    $ cd data-explore
    $ python setup.py develop

### Utilisation

After installation,
For any table within a database, the tool can be run entering the following command:

    $ data-explore --target=DATABASE --table=TABLE --output=LOG

The LOG file  produced by this command will contain all the information about the general structure of the TABLE held in DATABASE.

### Notation of the commands
DATABASE - Insert here the name of the database file that you want to import it needs to be in .db format
TABLE - Insert here the table within the database that need to be analysed
LOG - Insert here the name of the output file, this name needs to end with .log

### Test

If the tool needs to be tested after installing, enter the following commands:

  $  python -m pip install pytest. # If pytest is not already installed
  $  python -m pytest
