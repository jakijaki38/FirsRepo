from ncclient import manager
from xml.dom.minidom import parseString    #its built-in mdodule called xml.dom.mindon you do not need to import it actually gives python ability 
                                           # to do work with XML data and the funtion we will be use called it parseString so wr are going to 
                                           # convert RAW XML int Pretty XML then you will see particular data will print out in organise way.
from xmltodict import parse                # if you look that parituclar data you will see som unwanted data as well, to avaoid that we convert data in dictionary 
                                           # format(like e.g key is enable= vlaue of true etc like dictionary data) therefore we use from library xmltodict we import function 
                                           # called parse to convert all xml data into dictionarytype data.


xe = {
    'host': '192.168.195.131',
    'port': '830',
    'username' : 'admin',
    'password' : 'cisco',
    'hostkey_verify' : False
}

# XML filter 

netconf_filter = '''
<filter>
    <interfaces xmlns = "urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>

        </interface>
    </interfaces>
</filter>
'''

netconf = manager.connect(**xe)

# netconf has 3 funstions- 1. get , 2,get_config, 3. edict_config


query = netconf.get_config(filter = netconf_filter, source = 'running')  # from runing configure just filter interface
#print(query)                                                            #out put not easily readable
#print(parseString(query.xml).toprettyxml())                            #out is pretty and readbale
print(parse(query.xml))

#please see dict.py
#now i'm save in my dictioanry data in a variable to call e.g 

netconf_data = parse(query.xml)

all_interfaces = netconf_data['rpc-reply']['data']['interfaces']['interface']

# print(all_interfaces[1]['name'])

for interface in all_interfaces:
    print (interface['name'])
