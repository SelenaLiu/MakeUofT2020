import RPi.GPIO as GPIO
import time,requests
from multiprocessing import Process, Pipe
from threading import Thread
from motor import Motor
from sensor import Sensor

R_SERVO=4
SERVO_A=17
SERVO_B=27
TRIG_A=18
ECHO_A=23
TRIG_B=24
ECHO_B=16

state=True
threads=[]

sensorAData=[]
sensorBData=[]

if(__name__=="__main__"):
    with Motor(R_SERVO,SERVO_A,SERVO_B) as m, Sensor(TRIG_A,ECHO_A) as sensorA, Sensor(TRIG_B,ECHO_B) as sensorB:

        m.startMotors()
        motorThread=Thread(target=m.mainMotorLoop)
        #sensorAThread=Thread(target=sensorA.getDistance)
        #sensorBThread=Thread(target=sensorB.getDistance)
        #threads.append(motorThread)
        #threads.append(sensorAThread)
        #threads.append(sensorBThread)

        print("Starting threads")

        motorThread.start()
        #sensorAThread.start()
        #sensorBThread.start()
        while(True):
            sensorAData.append(sensorA.getDistance())
            sensorBData.append(sensorB.getDistance())
            print(sensorAData)
            print(sensorBData)
