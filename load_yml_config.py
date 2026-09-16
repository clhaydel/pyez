from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import yaml
from getpass import getpass

host=input("host: ")
user = input("username: ")
password = getpass("password: ")


dev = Device(host=host, user=user, password=password, gather_facts=False)
dev.open()

data = yaml.safe_load(open('protocol_data.yml'))

cu = Config(dev)

cu.load(template_path='protocol_temp.j2', template_vars=data, format='text')
cu.pdiff()
if cu.commit_check(timeout=90):
    cu.commit(timeout=90)
else:
    cu.rollback()

dev.close()
