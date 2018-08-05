#!/usr/bin/python3

# SoongSil Univ
# ESC
# Jwsong94

from gpiozero import *
from time import sleep

OSCIL_SENSOR = 5
FLAME_SENSOR = 6
SMOKE_SENSOR = 13

led = LED(17)

oscil = InputDevice(OSCIL_SENSOR);
flame = InputDevice(FLAME_SENSOR);
smoke = InputDevice(SMOKE_SENSOR);

def CheckOscillation( ) :
    print("Oscillation : ")
    return

def CheckFlame( ) :
    print("Flame : ")
    return

def CheckSmoke( ) :
    print("Smoke : ");
    return

while True:
    CheckOscillation()
    CheckFlame()
    CheckSmoke()
    led.on()
    sleep(1)
    led.off()
    sleep(1)
