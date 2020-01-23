from netmiko import ConnectHandler
from datetime import datetime

ios3= {
  'device_type': 'cisco_ios',
  'host': 'cisco3.lasthop.io',
  'username': 'pyclass',
  'password': '88newclass',
  'port': 22,
  'fast_cli': True,
}

net_connect = ConnectHandler(**ios3)

dns_config = ['ip name-server 1.1.1.1', 'ip name-server 1.0.0.1', 'ip domain-lookup']

start_time = datetime.now()

screen = net_connect.send_config_set(dns_config)

print(screen)
net_connect.disconnect()
stop_time = datetime.now()
print("elapsed time: {}".format(stop_time - start_time))
