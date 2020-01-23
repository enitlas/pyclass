from netmiko import ConnectHandler
ios4= {
  'device_type': 'cisco_ios',
  'host': 'cisco4.lasthop.io',
  'username': 'pyclass',
  'password': '88newclass',
  'port': 22,
}
net_connect = ConnectHandler(**ios4)

screen = net_connect.send_command("ping", expect_string=r"Protocol", strip_command=False)
screen += net_connect.send_command("\n", expect_string=r"Target IP", strip_prompt=False, strip_command=False)
screen += net_connect.send_command("8.8.8.8", expect_string=r"Repeat count", strip_prompt=False, strip_command=False)
screen += net_connect.send_command("\n", expect_string=r"Datagram size", strip_prompt=False, strip_command=False)
screen += net_connect.send_command("\n", expect_string=r"Timeout in seconds", strip_prompt=False, strip_command=False)
screen += net_connect.send_command("\n", expect_string=r"Extended commands", strip_prompt=False, strip_command=False)
screen += net_connect.send_command("\n", expect_string=r"Sweep range of sizes", strip_prompt=False, strip_command=False)
screen += net_connect.send_command("\n", expect_string=r"#", strip_prompt=False, strip_command=False)
net_connect.disconnect()

print()
print(screen)
print()
