#!/usr/bin/python3

# SoongSil Univ
# ESC
# Jwsong94

from gpiozero import LED
from time import sleep

led = LED(17)

def CheckOscillation( ) :
    print("Check Oscillation")
    return

def CheckFlame( ) :
    print("Check Flame")
    return

def CheckSmoke( ) :
    print("Check Smoke")
    return

while True:
    CheckOscillation()
    CheckFlame()
    CheckSmoke()
    led.on()
    sleep(1)
    led.off()
    sleep(1)
