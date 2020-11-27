from datetime import datetime
from time import sleep

# import the ORM items
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# import the Model classes for CPU and Storage
from db import EnvironmentTPH, Storage, Base

from random import gauss
# import the methods that will be used from the mypi file
from mypi import \
    get_serial, get_mac, get_host_name, \
    get_cpu_temp, get_gpu_temp, get_maximum_cpu_load

isPi = False

if isPi:
    from sense_hat import SenseHat


def headings():
    print()
    print(f'{"Name":<10}|{"Serial #":<18}|'
          f'{"MAC":<20}|{"Created at":<28}|'
          f'{"Temp":>10}|{"Humidity":>10}|'
          f'{"Pressure":>10}'
          f'')


db_filename = './data/monitor_data.db'
def main(_delay):
    engine = create_engine(f'sqlite:///{db_filename}')
    session = sessionmaker(bind=engine)()
    Base.metadata.create_all(engine)
    counter = 0

    while True:
        # Create a CPU object and set the properties

        environ = EnvironmentTPH()
        environ.host_name = get_host_name()
        environ.serial = get_serial()
        environ.host_mac = get_mac()
        environ.created_at = datetime.now()
        if isPi:
            sense = SenseHat()
            environ.pressure = sense.get_pressure()
            environ.temperature = sense.get_temperature()
            environ.humidity = sense.get_humidity()
        else:
            environ.pressure = get_pressure()
            environ.temperature = get_temperature()
            environ.humidity = get_humidity()


        session.add(environ)
        session.commit()

        last_readings = session.query(EnvironmentTPH).order_by(EnvironmentTPH.id.desc()).first()

        if counter % 10 == 0:
            headings()
        counter += 1

        print(f'{last_readings.host_name:<10}|{last_readings.serial:<18}|'
              f'{last_readings.host_mac:^20}|{last_readings.created_at}  |'
              f'{last_readings.pressure:>10.1f}|{last_readings.humidity:>10.1f}|'
              f'{last_readings.temperature:>10}'
              f'')

        sleep(_delay)

def get_pressure():
    return round(gauss(40, 10),2)


def get_humidity():
    return round(gauss(40, 10),2)


def get_temperature():
    return round(gauss(40, 10),2)

if __name__ == '__main__':
    delay = 5.0
    main(delay)