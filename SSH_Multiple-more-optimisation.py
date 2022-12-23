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

    user_choice = input("Welcome to the configuration Utiliy\n 1-Physical Interface\n 2-Loopback Interface\n Please choose the option:(1/2) ")
    if user_choice == str(1):
        Physical_int = input("Enter the Physical Interface Number: ")
        ip = input("Enter Ip address of the Interface: ")
        mask = input("Enter the subnet mask: ")
        commands = ("interface " + Physical_int, "ip address " + ip + " " + mask , "description loopback config from python by jawed", "no shutdown","end", "write")
        Physical = ssh.send_config_set(commands)
        print(Physical)

        output = ssh.send_command("show ip int br")
        print(output)

    elif user_choice == str(2):
        
        Loopback_int = input("Enter the Loopback Interface Number: ")
        ip = input("Enter Ip address of the Interface: ")
        mask = input("Enter the subnet mask: ")
        commands = ("interface loopback " + Loopback_int, "ip address " + ip + " " + mask , "description loopback config from python by jawed", "no shutdown","end", "write")
        Loopback = ssh.send_config_set(commands)
        print(Loopback)

        output = ssh.send_command("show ip int br")
        print(output)
    else:
        print("Invalid option please try again")





