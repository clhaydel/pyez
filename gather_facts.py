from jnpr.junos import Device
from pprint import pprint
from getpass import getpass

host=input("host: ")
user = input("username: ")
password = getpass("password: ")


dev = Device(host=host, user=user, password=password)
dev.open()

pprint(dev.facts)
