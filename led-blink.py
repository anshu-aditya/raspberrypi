#!/usr/bin/python3
# Purpose: A Simple Program to manipulate GPIO
# Author: Anshu Aditya
# Date: 20th Sep 2020
# last Modified: 20th Sep 2020

import RPi.GPIO as GPIO
import time

GPIO.cleanup() # cleanup all GPIOs
pin=11
GPIO.setmode(GPIO.BOARD) # BOARD pin-number scheme
GPIO.setup(pin,GPIO.OUT,initial=GPIO.LOW) # setting channel as output with inital value to LOW
while True:
	GPIO.output(pin,GPIO.HIGH) # at selected channel turn LED on
	time.sleep(0.1) # time delay 
	GPIO.output(pin,GPIO.LOW) # turn off
	time.sleep(0.1) 
#	GPIO.cleanup() # cleanup all GPIOs
