#!/usr/bin/python3

# SoongSil Univ
# ESC
# Jwsong94

import RPi.GPIO as GPIO
from time import sleep

class ESC_GPIO:
    def __init__(self):
        GPIO.setmode(GPIO.BCM);

        self.OSCIL_SENSOR = 5
        self.FLAME_SENSOR = 6
        self.SMOKE_SENSOR = 13

        GPIO.setup(self.OSCIL_SENSOR, GPIO.IN, GPIO.PUD_DOWN)
        GPIO.setup(self.FLAME_SENSOR, GPIO.IN, GPIO.PUD_DOWN)
        GPIO.setup(self.SMOKE_SENSOR, GPIO.IN, GPIO.PUD_DOWN)

        print("Init RPi.GPIO Version : " + GPIO.VERSION)

    def CheckOscillation(self) :
        # Normal : 1 / Oscil : 0
        if GPIO.input(self.OSCIL_SENSOR):
            print("Oscil : 1");
        else:
            print("Oscil : 0");
        #    print("Check Oscillation")
        return

    def CheckFlame(self) :
        # Normal : 1 / Flame : 0
        if GPIO.input(self.FLAME_SENSOR):
            print("Flame : 1")
        else:
            print("Flame : 0")
#    print("Check Flame")
        return

    def CheckSmoke(self) :
        # Normal : 1 / Smoke : 0
        if GPIO.input(self.SMOKE_SENSOR):
            print("Smoke : 1")
        else:
            print("Smoke : 0")
#    print("Check Smoke")
        return 


esc = ESC_GPIO();

while True:
#    esc.CheckOscillation()
#    esc.CheckFlame()
    esc.CheckSmoke()
    sleep(1)
