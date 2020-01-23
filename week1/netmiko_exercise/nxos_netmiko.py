
from netmiko import ConnectHandler

nxos1 = {
  'device_type': 'cisco_nxos',
  'host': 'nxos1.lasthop.io',
  'username': 'pyclass',
  'password': '88newclass',
  'port': 22,
}

nxos2= {
  'device_type': 'cisco_nxos',
  'host': 'nxos2.lasthop.io',
  'username': 'pyclass',
  'password': '88newclass',
  'port': 22,
}

dev_list= [nxos1, nxos2]

for i in dev_list:
    net_connect = ConnectHandler(**i)
    output = net_connect.send_command('show ip int brief')
    print(output)
