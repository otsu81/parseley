from parse_engine import ParseEngine


'''
Parseley is a stupid thing for me to learn some basic ETL for use in AWS
'''

def main():
    
    p = ParseEngine('test.csv',',')
    #p.print_something()
    p.read_file()



if __name__ == '__main__':
    main()

