import subprocess
import csv

command = ['ipmitool', 'dcmi', 'power', 'reading']
process = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        universal_newlines=True)
output = process.stdout
output = output.replace(' ', '').split('\n')
# Instantaneous_power_reading
print(output[1].split(':')[1].replace('Watts', ''))
# Minimum_during_sampling_period
print(output[2].split(':')[1].replace('Watts', ''))
# Maximum_during_sampling_period
print(output[3].split(':')[1].replace('Watts', ''))
# Average_power_reading_over_sample_period
print(output[4].split(':')[1].replace('Watts', ''))
# IPMI_time_stamp
print(output[5].split(':'))
# Day_of_Week
print(output[5].split(':')[1][:3])
# Month
print(output[5].split(':')[1][3:6])
# Day
print(output[5].split(':')[1][6])
# Time
print(output[5][21:29])
# Year
print(output[5][29:])
# Sampling_period
print(output[6].split(':')[1].replace('Seconds.', ''))
# Power_reading_state_is
print(output[7].split(':')[1])
print(output)

#with open('out_1.txt', 'r') as read, open('info.csv', 'w') as out:
#    write = csv.writer(out)
#    #write.writerow(row)
#    for line in read:
#        if line != '\n':
#            print(line.replace(' ', '').split(':')[1])

