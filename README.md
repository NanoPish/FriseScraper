# FriseScraper

Data gathering engine that harvests and save data from APIs and websites to feed LaFrise front-end.

## Installation

* Init sql user / db / table using `mysql -u root -p < init.sql` in the FriseScraper main dir
* Install the following dependencies using pip install in a virtualenv (selenium pymysql requests python-dateutil)

## Usage

* python sources/main.py

## More

* LaFrise.log contains program logs
* delete.sql removes all LaFrise related users / db / table from local mysql if used

# virtualenv how-to

* pip install virtualenv
* cd
* virtualenv LaFrise -p python3
* source ~/LaFrise/bin/activate
