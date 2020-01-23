from netmiko import ConnectHandler
ios4= {
  'device_type': 'cisco_ios',
  'host': 'cisco4.lasthop.io',
  'username': 'pyclass',
  'password': '88newclass',
  'port': 22,
}
net_connect = ConnectHandler(**ios4)

screen = net_connect.send_command_timing(
    "ping", strip_prompt=False, strip_command=False
)

screen += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
screen += net_connect.send_command_timing(
    "8.8.8.8", strip_prompt=False, strip_command=False
)
screen += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
screen += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
screen += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
screen += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
screen += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
net_connect.disconnect()

print()
print(screen)
print()
