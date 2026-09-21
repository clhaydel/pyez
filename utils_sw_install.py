from jnpr.junos import Device
from jnpr.junos.utils.sw import SW
from getpass import getpass

host=input("host: ")
user = input("username: ")
password = getpass("password: ")


dev = Device(host=host, user=user, password=password, gather_facts=False)
dev.open()

def update_progress(dev, report):
    print(dev.hostname, '> ', report)

sw = SW(dev)
ok = sw.install(package=r'/path/to/junos/jinstall-1x.1xxxx.tgz', progress=update_progress)
# progress takes boolean values too from 1.2.3 version onwards
#ok = sw.install(package=r'/Users/nitinkr/Downloads/jinstall-1x.1xxxx.tgz', progress=True)
if ok:
    print('rebooting')
    sw.reboot()
