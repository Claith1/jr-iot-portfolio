import jr_db
from time import sleep
from datetime import datetime
from random import gauss

def main(_delay):
    counter = 0
    while True:
        if counter == 0:
            print("LOAD | TEMP | TIME")
        counter += 1
        jr_db.AppendData(GetLoad(),GetTemp(),datetime.now())
        sleep(_delay)
def GetLoad():
    return gauss(50,20)

def GetTemp():
    return gauss(40, 10)

if __name__ == '__main__':
    delay = 5.0
    main(delay)

