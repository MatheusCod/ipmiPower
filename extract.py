import subprocess
import csv

command = ['ipmitool', 'dcmi', 'power', 'reading']
process = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        universal_newlines=True)
output = process.stdout
output = output.replace(' ', '').split('\n')
print(output[1].split(':')[1])

#with open('out_1.txt', 'r') as read, open('info.csv', 'w') as out:
#    write = csv.writer(out)
#    #write.writerow(row)
#    for line in read:
#        if line != '\n':
#            print(line.replace(' ', '').split(':')[1])

