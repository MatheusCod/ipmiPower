import threading
import sqlite3 as sql
import subprocess
import time
import os

# Delete current database file
try:
  os.remove("ipmi_data.db")
except OSError:
  pass
  
# Create database
conn = sql.connect('ipmi_data.db')
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS SensorData")
c.execute("CREATE TABLE SensorData (sensorRead TEXT, dataTime FLOAT)")
conn.commit()

# Class for threading
class saveDB(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
  def run(self, buffers, threadID):
    print("ThreadID:" + str(threadID))
    conn = sql.connect('ipmi_data.db')
    c = conn.cursor()
    for inst in buffers:
      newRow = " " + "(" + "\'" + str(inst[0].replace('\n', '\\n')) + "\'" + "," + str(inst[1]) + ")"
      newRow = "INSERT INTO SensorData VALUES" + newRow
      c.execute(newRow)
    conn.commit()
    conn.close()

# Create buffers
buffers = []
buffers.append([])
buffers.append([])

# Create thread
thread = saveDB()

# Complete buffer, after buffer is completed, use the other one while
# the first one is being saved on the database
bufferNumber = 0
i = 0
while i < 1002:
  
  # Get sensor value from ipmi
  sens = 'Total\n Power'
  command = ['sudo', 'ipmitool', 'sensor', 'get', sens]
  process = subprocess.run(
          command,
          stdout=subprocess.PIPE,
          universal_newlines=True)
  output = process.stdout
  output = output.replace('\n', '\\n')
  
  # Append on buffer
  buffers[bufferNumber].append([output, time.time()])
  
  # Checks if the current buffer is full
  if len(buffers[bufferNumber]) > 500:
    thread.run(buffers[bufferNumber], bufferNumber)
    buffers[bufferNumber] = []
    if bufferNumber == 0:
      bufferNumber = 1
    else:
      bufferNumber = 0
  i += 1

# Print database rows
#conn = sql.connect('ipmi_data.db')
#c = conn.cursor()
#for i in c.execute("SELECT * FROM SensorData"):
#  print(i)
