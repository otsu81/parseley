import os

class ParseEngine:
    def __init__(self,input_file,delimiter):
        self.inp = input_file
        self.delim = delimiter

    def print_something(self):
        print(self.delim)

    def read_file(self):
        rows = []
        with open(self.inp, 'r') as f:
            for line in f:
                print(line.split(self.delim))
                rows.append(line.split(self.delim))
        f.closed

        for line in rows:
            print(line)



    def get_map():
        pass

