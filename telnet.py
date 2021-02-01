from telnetlib import Telnet

host = "192.168.10.1"
password = "1234"


tn = Telnet(host)
tn.read_until(b'password')
tn.write(password.encoded('ascii')+b'\n')

tn.read_until(b'<Huawei>').decode('ascii')


tn.close()

tn.write(b'System view')

tn.write(b'VLAN 10')