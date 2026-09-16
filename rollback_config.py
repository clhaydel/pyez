from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from getpass import getpass

host = input("host: ")
user = input("username: ")
password = getpass("password: ")


dev = Device(host=host, user=user, password=password, gather_facts=False)
dev.open()

cu = Config(dev)
diff = cu.diff()
if diff:
    cu.rollback()
dev.close()


