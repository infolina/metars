# Metar fetching program to light LEDs

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

import xml.etree.ElementTree as ET
import time
import sys
import os

from neopixel import *

# LED strip configuration:
LED_COUNT      = 45      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

airportlist = ['keho','kakh','kuza','kdcm','klkr','keqy','kclt','kjqf','kipj','khky','ksvh','kruq','kexx','kint','kgso',
               'kbuy','kscr','ktta','khrj','kjnx','klhz','krdu','kigx','khbi','kvuj','kafp','kcqw','krcz','khff','ksop',
               'kfbg','kfay','kctz','klbt','kmeb','kfdw','kcub','kcdn','ksms','khvs','kflo','kmao','ksut','kilm', 'kpyg']

# Get the data for the airport
def getmetar(airportcode):
	url = "https://aviationweather.gov/adds/dataserver_current/httpparam?datasource=metars&requestType=retrieve&format=xml&mostRecentForEachStation=constraint&hoursBeforeNow=1&stationString="
	url = url + airportlist[airportcode]
	# print (url)
	print str(airportcode) + '. ' + airportlist[airportcode],
	content = urlopen(url).read()
	# print (content)
	metars = ET.fromstring(content)

	for metar in metars.iter('flight_category'):
		flightCat = metar.text
		print ' = ' + flightCat, 
		if flightCat == "VFR":
			return Color(255,0,0)
		elif flightCat == "MVFR":
			return Color(0,0,255)
		elif flightCat == "IFR":
			return Color(0,255,0)
		elif flightCat == "LIFR":
			return Color(0,125,125)
	return Color(0,0,0)



# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()
        mycol = Color(0,0,0)
        
	print ('Press Ctrl-C to quit.')
	for i in range(LED_COUNT):
		strip.setPixelColor(i, Color(255,255,255))
		strip.show()
		time.sleep(2)
		mycol = getmetar(i)
		print(mycol)
		strip.setPixelColor(i, mycol)
	print('Done!')
exit(0)
