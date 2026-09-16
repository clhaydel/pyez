from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from getpass import getpass

host=input("host: ")
user = input("username: ")
password = getpass("password: ")


dev = Device(host=host, user=user, password=password, gather_facts=False)
dev.open()

table = RouteTable(dev)
table.get()
#table.get('10.13.10.0/23', protocol='static')
print(table)
#for item in table:
#    print('destination:', item.key)
#    print('protocol:', item.protocol)
#    print('age:', item.age)
#    print('via:', item.via)

for route in table:
    destination = route.key  
    protocol = route.protocol
    nexthop = route.nexthop
    via = route.via
    print(f"{destination:<20} {protocol:<12} {str(nexthop):<15} {via}")

dev.close()
