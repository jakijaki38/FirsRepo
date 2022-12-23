from telnetlib import Telnet
from getpass import getpass

R1 = "192.168.0.46"
R2 = "192.168.0.47"
R3 = "192.168.0.48"


username = input("Enter you Username: ")
password = getpass("Enter you  assword: ")



all_device = [R1, R2, R3]


for device in all_device:
    tn = Telnet(device)
    tn.read_until(b"Username: ")
    tn.write(username.encode("ascii") + b"\n")

    tn.read_until(b"Password: ")
    tn.write(password.encode("ascii") + b"\n")

    print("Telent connection Established with " + device)


    tn.write(b"configure terminal\n")
    tn.write(b"interface loopback 20\n")
    tn.write(b"ip address 192.168.20.1 255.255.255.0\n")
    tn.write(b"description configured by Jawed using Python\n")
    tn.write(b"end\n")
    tn.write(b"write\n")
    tn.write(b"exit\n")
    

    print(tn.read_all().decode("ascii"))
  
