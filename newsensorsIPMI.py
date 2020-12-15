import subprocess

aux = 0

while True:
    command = ['sudo', 'ipmitool', 'sensor', 'get', 'Total Power']
    process = subprocess.run(
                command,
                stdout=subprocess.PIPE,
                universal_newlines=True)
    aux += 1
    print(aux)
        
