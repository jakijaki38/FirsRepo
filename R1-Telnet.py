import telnetlib

target = "192.168.0.46"
username = "admin"
password = "cisco1"


tn = telnetlib.Telnet(target)

tn.read_until(b"Username: ")
tn.write(username.encode('ascii') + b"\n")

tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")


print("Telenet connection with R1 thi wio ahay")

tn.write(b"configure terminal\n")
tn.write(b"interface loopback 10\n")
tn.write(b"ip address 192.168.1.1 255.255.255.0\n")
tn.write(b"description configured by jawed as first ever script for Automation using Python\n")

tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
