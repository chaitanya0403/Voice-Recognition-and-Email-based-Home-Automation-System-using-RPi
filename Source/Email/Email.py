if(len(x)<>O):
GPIO.setmode (GPIO.BOARD)
#signal to devices
if(x [O] == 'ONI'):
    Reply ('Turning ON switch 1’, y [O])
    GPIO.setup (7, GPIO.OUT)
    GPIO.output (7, GPI0.HIGH)		 #Turn ON LED1
if(x[O] == 'ON2'):
    Reply ('Turning ON switch 2', y [O])
    GPIO.setup (II, GPIO.OUT)
    GPIO.output (II, GPIO.HIGH)		 #Turn ON LED2
if(x[O] == 'ON3'):
    Reply ('Turning ON switch 3', y [O])
    GPIO.setup (12, GPIO.OUT)
    GPIO.output (12, GPI0.HIGH)		 #Turn ON LED3
if(x[O] == 'OFFI '):
    Reply ('Turning OFF switch 1', y [O])
    GPIO.setup (7, GPIO.OUT)
    GPIO.output (7, GPI0.LOW) 		#Turn OFF LEDI
if(x[O] == 'OFF2'):
    Reply ('Turning OFF switch 2', y [O])
    GPIO.setup (II, GPIO.OUT)
    GPIO.output (II, GPIO.LOW) 		#Turn OFF LED2
if(x[O] == 'OFF3'):
    Reply ('Turning OFF switch 3', y [O])
    GPIO.setup (12, GPIO.OUT)
    GPIO.output (12, GPI0.LOW) 		#Turn OFF LED3
time.sleep(O.S)					#call delay