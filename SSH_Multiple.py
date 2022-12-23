from netmiko import ConnectHandler

R1 = {"device_type":"cisco_ios",
"ip":"192.168.0.49",
"username":"admin",
"password":"cisco"
}

R2 = {"device_type":"cisco_ios",
"ip":"192.168.0.51",
"username":"admin",
"password":"cisco"
}

R3 = {"device_type":"cisco_ios",
"ip":"192.168.0.52",
"username":"admin",
"password":"cisco"
}

all_devices = [R1, R2, R3]

for device in all_devices:
    ssh = ConnectHandler(**device)
    print("Connection has been established with " + device["ip"])

    commands = ("interface loopback30", "ip address 1.1.1.1 255.255.255.255", "description loopback config from python by jawed", "no shutdown","end", "write")
    loopback = ssh.send_config_set(commands)
    print(loopback)


    output = ssh.send_command("show ip int br")

    print(output)


