import csv
from datetime import datetime
from sensordroid import Client


file = open('acc_readings.csv', 'w')
header = ['time', 'X-co', 'Y-co', 'Z-co']
writer = csv.DictWriter(file, fieldnames=header)
writer.writeheader()


def read_sensor_data():
    client = Client('192.168.43.1')
    client.sensorsReceived = client.connectSensors(port=0)
    client.connect()
    client.startDiscovery()
    if client.connected:
        print('Connected to {}'.format(client.address))
    else:
        print('Disconnected')

    #print('Displaying Accelerator readings in X, Y and Z co-ordinates:')

    #curr_time = time.localtime()
    #curr_clock = time.strftime("%H:%M:%S", curr_time)

    while True:
        data = client.dataCurrent.Acceleration.Values.AsString
        print(data)
        client.sensorsSampleRate = 1000
        y1, y2, y3 = data.split()
        time_now = datetime.now().strftime("%H:%M:%S")
        writer.writerow({'time': time_now, 'X-co': y1[0:5], 'Y-co': y2[0:5], 'Z-co': y3[0:5]})


read_sensor_data()



