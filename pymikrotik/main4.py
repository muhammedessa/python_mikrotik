import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.0.110', username='admin', password='')
stdin, stdout, stderr = client.exec_command('ip address add address 192.168.0.200/24 interface=ether2')

stdin, stdout, stderr =  client.exec_command('ip address print')
for line in stdout:
    print(line.strip('\n'))
client.close()


