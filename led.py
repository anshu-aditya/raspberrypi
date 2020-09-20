#!/usr/bin/python3
# Purpose: A Simple Program to manipulate GPIO
# Author: Anshu Aditya
# Date: 20th Sep 2020
# last Modified: 20th Sep 2020

import RPi.GPIO as GPIO
import time

GPIO.cleanup() # cleanup all GPIOs
pin=7
GPIO.setmode(GPIO.BOARD) # BOARD pin-number scheme
GPIO.setup(pin,GPIO.OUT)
GPIO.output(pin,GPIO.HIGH)
time.sleep(2) # 2 sec time-interval between on-and-off
GPIO.output(pin,GPIO.LOW)
GPIO.cleanup() # cleanup all GPIOs
