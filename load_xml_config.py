from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from getpass import getpass

host=input("host: ")
user = input("username: ")
password = getpass("password: ")


dev = Device(host=host, user=user, password=password, gather_facts=False)
dev.open()

cu = Config(dev)
data = """<policy-options>
          <policy-statement action="delete">
            <name>test-policy</name>
            <term>
                <name>test</name>
                <then>
                    <accept/>
                </then>
            </term>
            <from>
                <protocol>mpls</protocol>
            </from>
        </policy-statement>
        </policy-options>
        """


cu.load(data)
if cu.commit_check(timeout=90):
   cu.commit(timeout=90)
else:
   cu.rollback()
