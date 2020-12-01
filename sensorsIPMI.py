import sys
import subprocess
import time
import csv

#duration = sys.argv[1]
#file_name = sys.argv[2]
time_elapsed = 0

duration = 1
file_name = 'test'

with open(file_name + '.csv', 'w') as file_out:
    write = csv.writer(file_out)
    first_row = ['Sensor_ID', 'Sensor_Reading', 'Sensor_Reading_Unit', 'Status',
                 'Lower_Non_Recoverable', 'Lower_Critical',
                 'Lower_Non_Critical', 'Upper_Non_Critical', 'Upper_Critical',
                 'Upper_Non_Recoverable', 'Time_elapsed']
    write.writerow(first_row)
    end = time.time() + float(duration)
    while end > time.time():
        for sensor in sys.argv[3:]:
            command = ['sudo', 'ipmitool', 'sensor', 'get', sys.argv[i]]
            process = subprocess.run(
                    command,
                    stdout=subprocess.PIPE,
                    universal_newlines=True)
            output = process.stdout
            output = output.replace(' ', '').split('\n')
            current_row = []
            # Instantaneous_power_reading
            current_row.append(output[1].split(':')[1])
            print(current_row)
            #write.writerow(current_row)
