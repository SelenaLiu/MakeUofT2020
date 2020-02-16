import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
TRIG_A=18
ECHO_A=23
TRIG_B=24
ECHO_B=16
pulse_start = 0
pulse_end = 0

GPIO.setup(TRIG_A,GPIO.OUT)
GPIO.setup(ECHO_A,GPIO.IN)
GPIO.setup(TRIG_B,GPIO.OUT)
GPIO.setup(ECHO_B,GPIO.IN)

GPIO.output(TRIG_A,False)
GPIO.output(TRIG_B,False)

time.sleep(2)

def range(trig,echo):
    GPIO.output(trig,True)
    time.sleep(0.00001)
    GPIO.output(trig,False)
    pulse_start=0
    pulse_end=0
    #print(echo)
    while GPIO.input(echo)==0:
    	pulse_start=time.time()
    while GPIO.input(echo)==1:
    	pulse_end=time.time()
    pulse_duration = pulse_end-pulse_start
    time.sleep(0.05)	
    return pulse_duration

def get_distance(trig,echo):
    dn = range(trig,echo)
    distance = dn*17150
    return [distance, dn]

d = []
i = 0
total_time = 0

while(i<100):
    return_val = get_distance(TRIG_A,ECHO_A)
    d.append(return_val[0])
    total_time += return_val[1]
    #print("distance="+str(d))
    i+=1

print(d)
print(total_time)
GPIO.cleanup()

