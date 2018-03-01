#!/usr/bin/env python

############################################################
# sudo apt-get install git-core
# git clone https://github.com/adafruit/Adafruit_Python_DHT.git
# cd Adafruit_Python_DHT
# sudo apt-get install build-essential python-dev
# sudo python setup.py install
############################################################

import time
import Adafruit_DHT as dht

while True:
    h,t = dht.read_retry(dht.DHT22, 4)
    print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(t, h))
    exit()
