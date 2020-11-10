import sqlite3


def CreateTable():
    command = "create table  CPU (id integer primary key AUTOINCREMENT , load decimal, temperature decimal, created_at DateTime)"
    connection = sqlite3.connect("CPU.db")
    csr = connection.cursor()
    csr.execute(command)
    connection.commit()
    connection.close()


def AppendData(newLoad, newTemperature, newTime):
    command = "insert into CPU(load,temperature, created_at) value(" + str(newLoad) + "," + str(newTemperature) + "," + str(newTime) + ")"
    #connection = sqlite3.connect("CPUDatalog")
    #csr = connection.cursor()
    #csr.execute(command)
    #connection.commit()
   # connection.close()

    print(str(round(newLoad,2)) + " | " + str(round(newTemperature,2)) + " |" + str(newTime))