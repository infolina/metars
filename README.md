# metars
Quick little python project to fetch METARS from NOAA Aviation Weather

This program will fetch the METAR information and display the conditions using an LED strip.

To drive the LED's Download the code from:
https://github.com/jgarff/rpi_ws281x

To download the LED drivers do the following in the /home/pi folder:

sudo apt-get update

sudo apt-get install build-essential python-dev git scons swig

git clone https://github.com/jgarff/rpi_ws281x.git

cd rpi_ws281x

scons

cd python

sudo python setup.py install

You'll need to change the list of airports listed at the top to include the airports you want the METARS for.

The testandrun.sh can be added to /etc/rc.local to be run at bootup of the Pi simply add a line like this:

/home/pi/metars/testandrun.sh & 

Also add a line to your cron file to run /home/pi/metars/metar.sh once every 30 mins or 60 mins to get the latest data
  
