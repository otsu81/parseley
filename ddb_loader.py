from parse_engine import ParseEngine
from pynamo import AccountModel
from datetime import datetime
import os

"""Loads a file with specified delimiter into DynamoDB"""
# def main():
#     path = os.environ['HOME'] + '/Documents/wrkspc.py/organizations/extract_account_info/role_switch_urls.txt'
#     # load_table(path)
#     acc = AccountModel.get("628534059487")
#     print(acc.accountNbr + " " + acc.roleName)

"""Loads a CSV file into a dynamoDB table"""
def load_table(path):
    par = ParseEngine(path, ',')
    rows = par.get_rows()

    for line in rows:
        account = AccountModel(
            accountNbr = line[0][49:61], 
            roleName = line[0][71:], 
            description="Null",
            timestamp=datetime.now()
            )
        account.save()

"""Iterates over the entire index of hashkeys in the table"""
def iterate_table():
    for item in AccountModel.scan():
        print(item)

# if __name__ == '__main__':
#     main()
