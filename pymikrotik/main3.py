import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.0.110', username='admin', password='')
stdin, stdout, stderr = client.exec_command('ip firewall connection print')

for line in stdout:
    print(line.strip('\n'))
client.close()