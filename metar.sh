#!/bin/bash
echo "Changing dirs"
cd /home/pi/metars

echo "running metars"
sudo python metar.py

echo "finished"