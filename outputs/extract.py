import os.path
import sys
import time
import csv

with open('out_1.txt', 'r') as read, open('info.csv', 'w') as out:
    write = csv.writer(out)
    #write.writerow(row)
    for line in read:
        if line != '\n':
            print(line.replace(' ', '').split(':')[1])

