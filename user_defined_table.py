from jnpr.junos import Device
from jnpr.junos.factory.factory_loader import FactoryLoader
import yaml
from getpass import getpass

host = input("host: ")
user = input("username: ")
password = getpass("password: ")

yaml_data="""
---
ArpTable:
  rpc: get-arp-table-information
  item: arp-table-entry
  key: mac-address
  view: ArpView

ArpView:
  fields:
    mac_address: mac-address
    ip_address: ip-address
    interface_name: interface-name
    host: hostname
"""

dev = Device(host=host, user=user, password=password, gather_facts=False)
dev.open()

globals().update(FactoryLoader().load(yaml.safe_load(yaml_data)))
arps = ArpTable(dev)
arps.get()
for arp in arps:
        print('mac_address: ', arp.mac_address)
        print('ip_address: ', arp.ip_address)
        print('interface_name:', arp.interface_name)
        print('hostname:', arp.host)
  

dev.close()
