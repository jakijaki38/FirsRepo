#netmiko (3rd party Library) is the module that allows you create a SSH with netwrok device.
#in order to use Netmik command will be use from your local terminal/cmd or within pyton terminal window
#python3 -m pip install netmiko==2.4.2 (PIP "package installation manager" this command will allow you install 3rd party library 
#plus ""=="" would like to use stable version of netmik to avoid unstable of buggy ones.)
# verifcation of installtion of netmiko using command: python3 -m pip show netmiko
#


from netmiko import ConnectHandler                 #PYTHON -M PIP INSTALL NETMIKO==2.4.2   #using speckif funtion of netmiko called connectHandler

R1 = {
    'device_type':'cisco_ios',
    'ip': '192.168.0.49',
    'username': 'admin',
    'password': 'cisco'
}

ssh = ConnectHandler(**R1)
print ('\nSSH Session with R1 has been established.......\n')

#Netmiko uses 2funtions = 1.send_command(), 2.send_config_set()
#1.send_command() executes all the enable mode CLI commands on the device when passed as an arguments(see below example
#2.send_config_set executes all global config mode CLI commands on the device when passed as arguments


output = ssh.send_command("show ip interface brief")

print(output)

#output2 = ssh.send_config_set("configure terminal\n")

#print(output2)



