import sqlite3

class CPU():
    databaseName = "untitled"

    def CreateConnection(self):
        connection = sqlite3.connect("db_cpuMonitor")
        csr = connection.cursor()
        csr.execute("create table cpuCheck([id] integer primary key AUTOINCREMENT, [temperature] decimal,[created_at] DATETIME")
        connection.commit()
        connection.close()

    def InsertCPU(self,temperature, date):
        connection = sqlite3.connect("db_cpuMonitor")
        csr = connection.cursor()
        command = "insert into cpuCheck value (" + str(temperature) + "," + str(date) + ")"
        csr.execute(command)
        connection.commit()
        connection.close()