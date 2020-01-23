from netmiko import ConnectHandler
ios4= {
  'device_type': 'cisco_ios',
  'host': 'cisco4.lasthop.io',
  'username': 'pyclass',
  'password': '88newclass',
  'port': 22,
}
net_connect = ConnectHandler(**ios4)

#cisco_ios_show_lldp_neighbors_detail.textfsm

input_list = net_connect.send_command("show lldp neighbors detail", use_textfsm=True)
for item in input_list:
    print("Neighbor interface is:", item['neighbor_interface'])

net_connect.disconnect()
