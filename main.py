import boto3
from parse_engine import ParseEngine

def main():
    path = ""
    peng = ParseEngine(path, ',')
    peng.load_table()

if __name__ == '__main__':
    main()