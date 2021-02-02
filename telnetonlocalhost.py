from telnetlib import Telnet
import getpass

host = "http://localhost:8000/"
user = raw_input("Enter your remote account: ")
password = getpass.getpass()


tn = Telnet(host)
tn.read_until("login")
tn.write(user + "\n")
tn.read_until(b'password')
tn.write(password.encoded('ascii')+b'\n')

tn.read_until(b'<Huawei>').decode('ascii')


tn.close()

tn.write(b'System view')

tn.write(b'VLAN 10')