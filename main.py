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
GPIO.output(pin,True)

print("DONE")
#SETTING INITIAL VALUE AS TRUE AS RELAY IS TRIGGERED ON GROUND
lock_delay=3
# Capture SIGINT for cleanup when the script is aborted

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print ("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
 


# This loop keeps checking for RFID cards. If one is near it will get the UID and authenticate
while continue_reading:
    #Setting default Trigger for Relay
    GPIO.output(pin,True)
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print("Card detected")
        # Get the UID of the card
        time.sleep(0.6)
        (status,uid) = MIFAREReader.MFRC522_Anticoll()
        print(uid)
        #Authentication
        auth=software2.auth(uid)
        print(auth)
        if(auth==1):
                print("Welcome")
                #Trigerring Relay
                GPIO.output(pin,False)
                time.sleep(10)
        elif(auth==0):
                print("Unauthorized")

            
    time.sleep(0.1)

