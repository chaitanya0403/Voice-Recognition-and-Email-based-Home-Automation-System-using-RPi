import time
import datetime
import math
import sys, select, subprocess
import os
proc = subprocess.Popen(['sh', '-c', 'pocketsphinx_continuous -adcdev hw:1,0 -nfft 2048 -samprate 48000 2>/dev/null'],stdout=subprocess.PIPE)
while True:
    line = proc.stdout.readline()
    if line != '':
        output = line.rstrip()
        print output
        if (len(output.split("john"))>1):
            os.system('sudo python /home/pi/on.py')
        if (len(output.split("off"))>1):
            os.system('sudo python /home/pi/off.py')
        if (len(output.split("light"))>1):
            os.system('sudo python /home/pi/leds.py')
        if (len(output.split("hi"))>1):
            os.system('sudo python /home/pi/multiled.py')
    else:
        break
