from ncclient import manager

xe = {
    'ip':'192.168.195.130',
    'port':'830',
    'username': 'admin',
    'password': 'cisco'
}

netconf = manager.connect(
    host = xe['ip'],
    port = xe['port'],
    username = xe['username'],
    password = xe['password'],
    hostkey_verify = False
)

for abc in netconf.server_capabilities:

    print(abc)