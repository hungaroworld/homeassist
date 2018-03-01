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





ofile  = open('air3.csv', "wb")

try:
	
	writer=csv.writer(ofile)
	writer.writerow(title)

	for i in range(0,2520):
		h,t = dht.read_retry(dht.DHT22, 4)
		args=[datetime.datetime.now(),t,h]
		writer.writerow(args)
		time.sleep(10)

	