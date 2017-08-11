from pynamo import AccountModel
from datetime import datetime
import os

"""
Parses a CSV file and loads it into a DynamoDB table
"""
class ParseEngine():

    """Modular parsing engine"""
    def __init__(self, input_file, delimiter):
        """Init the class with input file and chosen delimiter"""
        self.inp = input_file
        self.delim = delimiter

    """returns all the rows of the CSV file in an array"""
    def get_rows(self):
        rows = []
        with open(self.inp, 'r') as f:
            for line in f:
                line = line.strip()
                rows.append(line.split(self.delim))
        
        return rows

    """
    Loads the parsed file into a dynamoDB table, which is specified by the
    AccountModel class
    """
    def load_table(self):
        rows = self.get_rows()

        for line in rows:
            account = AccountModel(
                accountNbr = line[0][49:61], 
                roleName = line[0][71:], 
                description="Null",
                timestamp=datetime.now()
                )
            account.save()

