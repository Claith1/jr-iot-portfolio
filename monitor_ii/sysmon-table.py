import jr_db
from time import sleep
from datetime import datetime
from random import gauss

def main():
    rows = jr_db.ReadData(10)
    print('{:10} {:10} {:20}'.format('Load','Temperature','Create_Date'))
    for row in rows:
        string = '{:10} {:10} {:20}'.format(str(row[0]),str(row[1]),str(row[2]))
        print(string)

if __name__ == '__main__':
    main()


