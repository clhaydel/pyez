from jnpr.junos import Device
from lxml import etree
from getpass import getpass

host=input("host: ")
user = input("username: ")
password = getpass("password: ")


dev = Device(host=host, user=user, password=password, gather_facts=False)
dev.open()

op = dev.rpc.get_interface_information()
#op = dev.rpc.get_interface_information({'format': 'text'})
#op = dev.rpc.get_interface_information(interface_name='lo0', terse=True)
print(etree.tostring(op))

#for i in op.xpath('.//link-level-type'):
#    print i.text
dev.close()
