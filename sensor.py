
import RPi.GPIO as GPIO
import time


class Sensor():

    def __init__(self,trigval,echoval):

        self.TRIG=trigval
        self.ECHO=echoval
        self.delay=0.01
        GPIO.setmode(GPIO.BCM)
        self.initializeSensors()

        

    def __enter__(self):
        return self

    def initializeSensors(self):

        GPIO.setup(self.TRIG,GPIO.OUT)
        GPIO.setup(self.ECHO,GPIO.IN)

        GPIO.output(self.TRIG,False)
        time.sleep(0.5)

    def getRange(self):
        GPIO.output(self.TRIG,True)
        time.sleep(0.00001) #10uS Pulse
        GPIO.output(self.TRIG,False)
        pulse_start=0
        pulse_end=0
        while GPIO.input(self.ECHO)==0:
            pulse_start=time.time()
        while GPIO.input(self.ECHO)==1:
            pulse_end=time.time()
        pulse_duration = pulse_end-pulse_start
        time.sleep(self.delay)	
        return pulse_duration

    def getDistance(self):
        dn = self.getRange()
        distance = dn*(343*100/2)
        return distance#[distance, dn]


#d = []
#i = 0
#total_time = 0

#while(i<100):
#    return_val = get_distance(TRIG_A,ECHO_A)
#    d.append(return_val[0])
#    total_time += return_val[1]
#    #print("distance="+str(d))
#    i+=1

#print(d)
#print(total_time)
#GPIO.cleanup()

    def __exit__(self,exc_type,exc_value,traceback):
        GPIO.cleanup()

    def __del__(self):
        GPIO.cleanup()


if(__name__=="__main__"):
    s = Sensor(24,16)
    print(s.getDistance())
