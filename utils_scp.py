from jnpr.junos import Device
from jnpr.junos.utils.scp import SCP
from getpass import getpass

host=input("host: ")
user = input("username: ")
password = getpass("password: ")


dev = Device(host=host, user=user, password=password, gather_facts=False)
dev.open()

with SCP(dev, progress=True) as scp:
         scp.get('/var/tmp/file.txt','file.txt')
dev.close()
