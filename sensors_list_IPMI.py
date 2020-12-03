import sys
import subprocess
import time
import csv

duration = sys.argv[1]
file_name = sys.argv[2]
sensors = sys.argv[3:]
time_begin = time.time()

new_sensors = []
for i in range(len(sensors)):
    new_sensors.append(sensors[i].replace(' ', ''))

#duration = 1
#file_name = 'test'

with open(file_name + '.csv', 'w') as file_out:
    write = csv.writer(file_out)
    first_row = ['Sensor_ID', 'Sensor_Reading', 'Sensor_Reading_Unit', 'Status',
                 'Lower_Non_Recoverable', 'Lower_Critical',
                 'Lower_Non_Critical', 'Upper_Non_Critical', 'Upper_Critical',
                 'Upper_Non_Recoverable', 'Time_elapsed']
    write.writerow(first_row)
    end = time.time() + float(duration)
    while end > time.time():
        command = ['sudo', 'ipmitool', 'sensor', 'list']
        process = subprocess.run(
                    command,
                    stdout=subprocess.PIPE,
                    universal_newlines=True)
        output = process.stdout
        output = output.replace(' ', '')
        output = output.split('\n')
        for i in range(len(output)):
            output[i] = output[i].split('|')
        current_row = []
        for row in output:
            current_row = []
            if (row[0] in new_sensors):
                current_row = row
                current_row.append("{:.5f}".format(time.time() - time_begin))
                write.writerow(current_row)
