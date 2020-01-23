import time
from netmiko import ConnectHandler

ios4 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": '88newclass',
    "secret": '88newclass',
    "device_type": "cisco_ios",
    "session_log": "my_output.txt",

}

net_connect = ConnectHandler (**ios4)
screen = net_connect.config_mode()
print(screen)
screen1 = net_connect.find_prompt()
print(screen1)
screen5 = net_connect.exit_config_mode()
print(screen5)
screen2 = net_connect.write_channel('disable\n')
print(screen2)
time.sleep(5)
screen3 = net_connect.read_channel()
print(screen3)
net_connect.enable()
screen4 = net_connect.find_prompt()
print(screen4)
net_connect.disconnect()
