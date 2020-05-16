##########################################################
# Auther:Sachin
# Date of created: 16/3/2020
##########################################################

import RPi.GPIO as IO   #calling header file for GPIO of PI
import time             #calling for time to provide delays in program
IO.setmode(IO.BOARD)    #programming the GPIO by BOARD pin numbers GPIO21 is called as PIN40
IO.setwarnings(False)  
IO.setup(40,IO.OUT)     #intiallize digital pin40 as an output
IO.setup(38,IO.OUT)     #intiallize digital pin40 as an output
IO.setup(36,IO.OUT)     #intiallize digital pin40 as an output
IO.setup(37,IO.OUT)     #intiallize digital pin40 as an output
IO.output(40,0)
IO.output(38,0)
IO.output(37,0)
IO.output(36,0)
LED1 = '1'
LED2 = '2'
LED3 = '3'
LED4 = '4'
LED_select = 0
value = 0;
while (1):
    value = input("Enter the LED number to glow\n")  #prompt user to enter
    if value == LED1 or value == LED2 or value == LED3 or value == LED4:
        LED_select = value
        print("you are selected LED " +LED_select)
    if  LED_select == LED1:
        IO.output(40,1)         #turn the LED on (making the voltage level HIGH)
        time.sleep(1)           # sleep for 1 second
        print ("LED1 glow ON")
        IO.output(40,0)         #turn the LED on (making the voltage level LOW)
        time.sleep(1)           # sleep for 1 second
        print ("LED1 glow OFF")
    elif LED_select == LED2:
        IO.output(38,1)         #turn the LED on (making the voltage level HIGH)
        time.sleep(1)           # sleep for 1 second
        print ("LED2 glow ON")
        IO.output(38,0)         #turn the LED on (making the voltage level LOW)
        time.sleep(1)           # sleep for 1 second
        print ("LED2 glow OFF")
    elif  LED_select == LED3:
        IO.output(37,1)         #turn the LED on (making the voltage level HIGH)
        time.sleep(1)           # sleep for 1 second
        print ("LED3 glow ON")
        IO.output(37,0)         #turn the LED on (making the voltage level LOW)
        time.sleep(1)           # sleep for 1 second
        print ("LED3 glow OFF")
    elif  LED_select == LED4:
        IO.output(36,1)         #turn the LED on (making the voltage level HIGH)
        print ("LED4 glow ON")
        time.sleep(1)           # sleep for 1 second   
        IO.output(36,0)         #turn the LED on (making the voltage level LOW)
        print ("LED4 glow OFF")

