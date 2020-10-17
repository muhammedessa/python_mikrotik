from librouteros import connect

api = connect(username='admin', password='', host='192.168.0.111')
ip_info = api(cmd="/ip/address/print")

for item in ip_info:
    print(item)
