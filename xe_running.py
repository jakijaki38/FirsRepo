from ncclient import manager
from xml.dom.minidom import parseString


xe = {
    'host': '192.168.195.130',
    'port': '830',
    'username' : 'admin',
    'password' : 'cisco',
    'hostkey_verify' : False
}


netconf = manager.connect(**xe)

# netconf has 3 funstions- 1. get , 2,get_config, 3. edict_config


query = netconf.get_config(source = 'running')
print(query)                                            #out put not easily readable
print(parseString(query.xml).toprettyxml())                #out is pretty and readbale

