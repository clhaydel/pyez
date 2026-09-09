from jnpr.junos.utils.fs import FS
from jnpr.junos import Device
from getpass import getpass

host=input("host: ")
user = input("username: ")
password = getpass("password: ")

dev = Device(host=host, user=user, password=password)
dev.open()

fs = FS(dev)
print(fs.ls('/var/tmp'))

dev.close()
