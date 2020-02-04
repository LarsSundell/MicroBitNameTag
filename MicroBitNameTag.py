from microbit import *
import radio

radio.on()
radio.config(queue=1, channel=7, power=5) #Store 1 package, set channel and output power
myName = "ADA" # use variable for name

while True:
    # display own name
    display.scroll("MY NAME IS %s" %(myName), delay=80) # used delay to control speed
    # Broadcast name to other Microbits
    radio.send_bytes(myName)
    sleep(500) # add a short (500 ms) pause before starting over
    # check if a name has been received
    received = radio.receive_full() # returns None if nothing is received
    if received: # A packet has been received
        msg, rssi, timeStamp = received
        received = str(msg, 'utf-8') #convert to string
        if (rssi > -60): # only greet if person is close
            display.scroll("HELLO %s" %(received), delay=80)
        sleep(500) # short pause
