import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM);

GPIO.setup(16, GPIO.OUT);

buzzer = GPIO.PWM(16, 3000);
buzzer.start(0);

buzzer.ChangeDutyCycle(90);

while True:
    print("");

