from jnpr.junos import Device
from lxml import etree
from getpass import getpass

host = input("host: ")
user = input("username: ")
password = getpass("password: ")


dev = Device(host=host, user=user, password=password, gather_facts=False)
dev.open()

cnf = dev.rpc.get_config()
#cnf = dev.rpc.get_config(filter_xml=etree.XML('<configuration><interfaces/></configuration>'))
#print(etree.tostring(cnf))
print(etree.tostring(cnf, pretty_print=True).decode())
