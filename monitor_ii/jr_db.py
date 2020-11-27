import sqlite3
def CreateTable():

    command = "create table  CPU (id integer primary key AUTOINCREMENT, load decimal, temperature decimal, decimal humidity, decimal pressure  created_at DateTime)"
    connection = sqlite3.connect("CPU.db")
    csr = connection.cursor()
    csr.execute(command)
    connection.commit()
    connection.close()


def AppendData(newLoad, newTemperature, newTime):
    try:
        command = "insert into CPU(load,temperature, created_at) values" \
                  " (" + str(round(newLoad,2)) + "," + str(round(newTemperature,2)) + ",'" + str(newTime) + "')"
        #print(command)
        connection = sqlite3.connect("CPU.db")
        csr = connection.cursor()
        csr.execute(command)
        connection.commit()
        connection.close()
        print(str(round(newLoad, 2)) + " | " + str(round(newTemperature, 2)) + " |" + str(newTime))
    except Exception as e:
        print(e)


def ReadData(count = 5,):
    command = "select load, temperature, created_at from CPU order by created_at desc limit " + str(count)
    connection = sqlite3.connect("CPU.db")
    csr = connection.cursor()
    csr.execute(command)
    rows = csr.fetchall()
    return rows