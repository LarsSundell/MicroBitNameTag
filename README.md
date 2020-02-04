# MicroBitNameTag
Code for using the Micro:bit as a nametag that will greet other persons with the same tag with their own name

The code will scroll your name on the microbit screen. As soon as another micro:bit with the same code is in range, your micro:bit will greet that person with an "Hello" followed by the name of the person. 

You need at lest 2 micro:bits for this project.
You will need to change the myName variable for each of the micro:bit's in use to reflect the name of the person carrying it as a name tag.

The code uses the RSSI signal strength to decide if the other person is "close enough" the default setting will consider ~2 meters as "close enough", but that depends on a lot of factors, so some experimenting with the threshold might be needed.

To download the code to your microbit you may use the online editor at https://www.microbit.org/
Direct link to the editor: https://python.microbit.org/v/2.0

Feel free to copy and modify the code
