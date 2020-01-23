
from netmiko import ConnectHandler

ios3= {
  'device_type': 'cisco_ios',
  'host': 'cisco3.lasthop.io',
  'username': 'pyclass',
  'password': '88newclass',
  'port': 22,
}

dev_list= [ios3]

for i in dev_list:
    net_connect = ConnectHandler(**i)
    output = net_connect.send_command('show version')

with open('showver.txt', 'w') as buff:
    print(output, file=buff)
buff.close
