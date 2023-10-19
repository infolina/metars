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
LED_COUNT      = 104      # Number of LED pixels.
METAR_COUNT    = 99      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

airportlist = ['kmia','korl','ktpa','kjax','ktlh','ksav','kchs','kags','kcae','kmyr',
	'kilm','krdu','kgso','kclt','kgmu','kavl','ktys','katl','kbhm','khsv',
	'kbna','klou','klex','kcvg','kstl','kind','kfwa','kgrr','kdet','kcle',
	'kpit','kbuf','kroc','ksyr','kalb','kbtv','kbgr','kpwm','kbos','kmvy',
	'kpvd','khfd','kbdr','kjfk','kacy','kphl','kbwi','kiad','kric','korf',
	'kwwd','kcrw','kmem','klit','kjan','kbix','knew','kiah','kcrp','kodo',
	'kabq','kfmn','kgjt','kden','kcys','kslc','kflg','kphx','klax','ksan',
	'klas','krno','ksfo','kfat','kboi','ksea','kpdx','keug','kmso','kgeg',
	'kbil','kjac','krap','kbis','kord','kmke','kosh','kmsp','kfar','kfsd',
	'koma','kdsm','kmci','kict','ktul','kokc','kdfw','kshv','kvuj']

# Get the data for the airport
def getmetar(airportcode):
	url = "https://aviationweather.gov/cgi-bin/data/dataserver.php?requestType=retrieve&hoursBeforeNow=4&format=xml&mostRecent=true&dataSource=metars&stationString="
	url = url + airportlist[airportcode]
	# print (url)
	print str(airportcode) + '. ' + airportlist[airportcode],

	try:
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
	except Exception as exc:
		print('There was a problem: %s' % (exc))

	return Color(0,0,0)



# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()
        mycol = Color(0,0,0)
        
	strip.setPixelColor(99, Color(255,255,255))
	strip.setPixelColor(99,Color(255,0,0))
	strip.show()	
	strip.setPixelColor(100, Color(255,255,255))
	strip.setPixelColor(100,Color(0,0,255))	
	strip.show()
	strip.setPixelColor(101, Color(255,255,255))
	strip.setPixelColor(101,Color(0,255,0))	
	strip.show()
	strip.setPixelColor(102, Color(255,255,255))
	strip.setPixelColor(102,Color(0,125,125))
	strip.show()
	
	for i in range(METAR_COUNT):
		strip.setPixelColor(i, Color(255,255,255))
		strip.show()
		time.sleep(.5)
		mycol = getmetar(i)
		print(mycol)
		strip.setPixelColor(i, mycol)
		strip.show()
	strip.setPixelColor(99, Color(255,255,255))
	strip.setPixelColor(99,Color(255,0,0))
	strip.show()	
	strip.setPixelColor(100, Color(255,255,255))
	strip.setPixelColor(100,Color(0,0,255))	
	strip.show()
	strip.setPixelColor(101, Color(255,255,255))
	strip.setPixelColor(101,Color(0,255,0))	
	strip.show()
	strip.setPixelColor(102, Color(255,255,255))
	strip.setPixelColor(102,Color(0,125,125))	

print('Done!')
exit(0)
