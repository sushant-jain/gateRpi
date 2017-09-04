#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import time
import software2

continue_reading = True
#SETTING UP GPIO BOARD
pin =32
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin,GPIO.OUT)   #SETTING PIN 29 AS OUTPUT PIN TO RELAY 
GPIO.output(pin,GPIO.LOW)

print("DONE")
#SETTING INITIAL VALUE AS TRUE AS RELAY IS TRIGGERED ON GROUND
lock_delay=3
# Capture SIGINT for cleanup when the script is aborted



# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
 


# This loop keeps checking for RFID cards. If one is near it will get the UID and authenticate
while continue_reading:
    #Setting default Trigger for Relay
    GPIO.output(pin,GPIO.LOW)
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print("Card detected")
        # Get the UID of the card
        time.sleep(0.6)
        (status,uid) = MIFAREReader.MFRC522_Anticoll()
        print(uid)
        time.sleep(3) 
        #Authentication
        auth=software2.auth(uid)
        if(auth==1):
                print("Welcome")
                #Trigerring Relay
                GPIO.output(pin,GPIO.HIGH)
                time.sleep(lock_delay)
        elif(auth==0):
                print("Unauthorized")

            
    time.sleep(0.1)
GPIO.cleanup()
