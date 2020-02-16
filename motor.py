import RPi.GPIO as GPIO
import time

class Motor():

    def __init__(self,rservo,servoa,servob):
        self.R_SERVO=rservo
        self.T_SERVO_A=servoa
        self.T_SERVO_B=servob
        GPIO.setmode(GPIO.BCM)
        self.initializeMotors()
        self.resetPosition()
        self.stopMotion()

    def __enter__(self):
        return self

    def initializeMotors(self):
        GPIO.setup(self.R_SERVO,GPIO.OUT)
        GPIO.setup(self.T_SERVO_A,GPIO.OUT)
        GPIO.setup(self.T_SERVO_B,GPIO.OUT)

        self.p = GPIO.PWM(self.R_SERVO,50)
        self.sa = GPIO.PWM(self.T_SERVO_A,50)
        self.sb = GPIO.PWM(self.T_SERVO_B,50)

    def startMotors(self):
        self.p.start(2.5)
        self.sa.start(2.5)
        self.sb.start(2.5)

    def moveMotorA(self,val):
        self.sa.ChangeDutyCycle(val)

    def moveMotorB(self,val):
        self.sb.ChangeDutyCycle(val)
    
    def moveMotorR(self,val):
        self.p.ChangeDutyCycle(val)
        
    def tilt(self,val):
        self.moveMotorA(val)
        self.moveMotorB(val)

    def resetPosition(self):
        self.tilt(2)
        self.moveMotorR(2)

    def stopMotion(self):
        self.tilt(0)
        self.moveMotorR(0)

    def mainMotorLoop(self):
        while(True):#TODO: Add end condition
            time.sleep(1)
            self.moveMotorR(12.5)
            self.tilt(0)
            time.sleep(1)
            self.tilt(2)
            #p.ChangeDutyCycle(5)
            #time.sleep(0.5)
            #p.ChangeDutyCycle(5)
            
            self.tilt(4)
            
            time.sleep(1)
            self.moveMotorR(2.5)
            
            time.sleep(0.5)
            
            self.tilt(2)

    def __exit__(self,exc_type,exc_value,traceback):
        self.stopMotion()
        self.p.stop()
        self.sa.stop()
        self.sb.stop()
        GPIO.cleanup()

    def __del__(self):
        print("deleting motor object")
        self.stopMotion()
        p.stop()
        sa.stop()
        sb.stop()
        GPIO.cleanup()
