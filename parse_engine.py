import os

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

    def get_map(self):
        pass

