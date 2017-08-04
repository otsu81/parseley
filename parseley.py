from parse_engine import ParseEngine
from pynamo import AccountModel
from datetime import datetime
import os

"""Parseley is a stupid thing for me to learn some basic ETL for use in AWS"""
def main():
    load_table()

"""Loads a CSV file into a dynamoDB table"""
def load_table():
    par = ParseEngine(os.environ['HOME'] + '/Documents/wrkspc.py/parseley/test.csv', ',')
    rows = par.get_rows()

    for line in rows:
        account = AccountModel(
            accountNbr=line[0], 
            roleName=line[1], 
            description=line[2],
            timestamp=datetime.now()
            )
        account.save()

"""Iterates over the entire index of hashkeys in the table"""
def iterate_table():
    for item in AccountModel.scan():
        print(item)

"""Test to get item"""
def get_account(nbr):
    print(AccountModel.get('q'))


if __name__ == '__main__':
    main()
