import csv
import matplotlib.pyplot as plt
import matplotlib.figure as fig

avg = []
time_elapsed = []
with open('test10x.csv', 'r') as file_in:
    read = csv.reader(file_in)
    for line in read:
        break
    for line in read:
        avg.append(int(line[3]))
        time_elapsed.append(int(line[11].lstrip('0')))
    #plt.plot(avg, time)
    #plt.show()

plt.plot(time_elapsed, avg)
plt.title("POWER9 power consumption ")
plt.ylabel('Average power reading in Watts')
plt.xlabel('Time in millisecons')
fig = plt.gcf()
fig.set_size_inches(8, 6)
plt.savefig('powerConsumption.png', dpi=100)
#plt.show()
