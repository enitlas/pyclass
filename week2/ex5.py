from netmiko import ConnectHandler

nxos1 = {
  'host': 'nxos1.lasthop.io',
  'device_type': 'cisco_nxos',
  'username': 'pyclass',
  'password': '88newclass',
  'port': 22,
}

nxos2 = {
  'device_type': 'cisco_nxos',
  'host': 'nxos2.lasthop.io',
  'username': 'pyclass',
  'password': '88newclass',
  'port': 22,
}

for dev in (nxos1, nxos2):
  net_connect = ConnectHandler(**dev)
  screen = net_connect.send_config_from_file('ex5_file.txt')
  print(screen)
  net_connect.save_config()
  net_connect.disconnect()
