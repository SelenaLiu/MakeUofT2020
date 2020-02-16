import RPi.GPIO as GPIO
import time

R_SERVO = 4
T_SERVO_A=17
T_SERVO_B=27

TRIG_A=18
ECHO_A=23
TRIG_B=24
ECHO_B=16
pulse_start = 0
pulse_end = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(R_SERVO,GPIO.OUT)
GPIO.setup(T_SERVO_A,GPIO.OUT)
GPIO.setup(T_SERVO_B,GPIO.OUT)

GPIO.setup(TRIG_A,GPIO.OUT)
GPIO.setup(ECHO_A,GPIO.IN)
GPIO.setup(TRIG_B,GPIO.OUT)
GPIO.setup(ECHO_B,GPIO.IN)

GPIO.output(TRIG_A,False)
GPIO.output(TRIG_B,False)

p = GPIO.PWM(R_SERVO,50)
sa = GPIO.PWM(T_SERVO_A,50)
sb = GPIO.PWM(T_SERVO_B,50)
p.start(2.5)
sa.start(2.5)
sb.start(2.5)

try:
    while(True):
        time.sleep(1)
        p.ChangeDutyCycle(12.5)
        sa.ChangeDutyCycle(0)
        sb.ChangeDutyCycle(0)
        time.sleep(1)
        sa.ChangeDutyCycle(2)
        sb.ChangeDutyCycle(2)
        
        #p.ChangeDutyCycle(5)
        #time.sleep(0.5)
        #p.ChangeDutyCycle(5)
        
        
        sa.ChangeDutyCycle(4)
        sb.ChangeDutyCycle(4)
        
        time.sleep(1)
        p.changeDutyCycle(2.5)
        
        time.sleep(0.5)
        
        sa.ChangeDutyCycle(2)
        sb.ChangeDutyCycle(2)
    
except:
    p.stop()
    GPIO.cleanup()

p.stop()
GPIO.cleanup()
