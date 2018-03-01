import Adafruit_DHT as dht
import datetime
import time
import csv
import dbus
import onedrivesdk
from onedrivesdk.helpers import GetAuthCodeServer

title=['Time', 'Temperature', 'Humidity']
redirect_uri = "http://localhost:8080/"
client_secret = "b016ZXPsQ9aC9O5om9FCCXA"

client = onedrivesdk.get_default_client(client_id='55ebd19b-941c-4779-8847-a661f1cac052', scopes=['wl.signin', 'wl.offline_access', 'onedrive.readwrite'])
auth_url = client.auth_provider.get_auth_url(redirect_uri)

 # Block thread until we have the code
code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)
# Finally, authenticate!
client.auth_provider.authenticate(code, redirect_uri, client_secret)



ofile  = open('air3.csv', "wb")

try:
	
	writer=csv.writer(ofile)
	writer.writerow(title)

	for i in range(0,2520):
		h,t = dht.read_retry(dht.DHT22, 4)
		args=[datetime.datetime.now(),t,h]
		writer.writerow(args)
		time.sleep(10)
finally:
	ofile.close()

	#My Application Id:
#(55ebd19b-941c-4779-8847-a661f1cac052)
	#My application secret password/key:
#(b016ZXPsQ9aC9O5om9FCCXA)
#Application Name:
#AirQ

returned_item = client.item(drive="me", id="root").children['air3.csv'].upload('air')


#sys_bus = dbus.SystemBus()
#ck_srv = sys_bus.get_object('org.freedesktop.ConsoleKit','/org/freedesktop/ConsoleKit/Manager')
#ck_iface = dbus.Interface(ck_srv, 'org.freedesktop.ConsoleKit.Manager')
#stop_method = ck_iface.get_dbus_method("Stop")
#stop_method()

	