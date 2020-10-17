#Allow SSH

import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.0.111', username='admin', password='')
stdin, stdout, stderr = client.exec_command('/ip firewall nat add action=dst-nat chain=dstnat dst-port=5022 protocol=tcp to-addresses=192.168.100.22 to-ports=22')

for line in stdout:
    print(line.strip('\n'))
client.close()