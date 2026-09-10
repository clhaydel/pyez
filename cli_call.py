from jnpr.junos import Device
from getpass import getpass

host=input("host: ")
user = input("username: ")
password = getpass("password: ")


with Device(host=host, user=user, password=password) as dev:
    print(dev.cli("show version", warning=False))

