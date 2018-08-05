#!/usr/bin/python3

# SoongSil Univ
# ESC
# Jwsong94

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM);

OSCIL_SENSOR = 5
FLAME_SENSOR = 6
SMOKE_SENSOR = 13

GPIO.setup(OSCIL_SENSOR, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(FLAME_SENSOR, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(SMOKE_SENSOR, GPIO.IN, GPIO.PUD_DOWN)

print("Init RPi.GPIO Version : " + GPIO.VERSION)

def CheckOscillation( ) :
    if GPIO.input(OSCIL_SENSOR):
        print("Oscil : 1");
    else:
        print("Oscil : 0");
#    print("Check Oscillation")
    return

def CheckFlame( ) :
    if GPIO.input(FLAME_SENSOR):
        print("Flame : 1")
    else:
        print("Flame : 0")
#    print("Check Flame")
    return

def CheckSmoke( ) :
    if GPIO.input(SMOKE_SENSOR):
        print("Smoke : 1")
    else:
        print("Smoke : 0")
#    print("Check Smoke")
    return 

while True:
    CheckOscillation()
#    CheckFlame()
#    CheckSmoke())
    sleep(1)
