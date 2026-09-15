from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from getpass import getpass

host=input("host: ")
user = input("username: ")
password = getpass("password: ")


dev = Device(host=host, user=user, password=password, gather_facts=False)
dev.open()

cu = Config(dev)
data = """interfaces { 
    ge-0/0/0 {
        description "CONFIG TEST";
    } 
}
"""
cu.load(data, format='text')
cu.pdiff()
if cu.commit_check(timeout=90):
   cu.commit(timeout=90)
else:
   cu.rollback()
