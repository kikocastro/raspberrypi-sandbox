import time, os
try:

#Make sure we can import the GPIO library
	import RPi.GPIO as GPIO

except RuntimeError:
	print ("Unable to import GPIO library.  Make sure that this is being run as root and that RPi.GPIO is properly installed!")

#Pins will be referenced by the processor's numbering scheme
GPIO.setmode(GPIO.BCM)

#Tell the program you want to use pin number 22 as the input
GPIO.setup(22, GPIO.IN)

#Set up a function to check the state of the GPIO pin
def waitcheck():

	loop=1
	print ("When you're ready, please press the button. . . ")
	while (loop):

	#Run as long as loop is nonzero and check the state of the button ten times per second
		time.sleep(0.1)

	#If the button is pressed
		if(GPIO.input(22)==0):

		#Cleanup GPIO since it is no longer needed
			GPIO.cleanup()

		#Do not loop again
			loop=0

		#Say the cow is coming
			print ("Here comes the cow!")

		#Actually play the sound
			os.system("omxplayer -o hdmi cow.mp3")

try:
	#call function, this will run forever
	waitcheck()
	#Exit this program if control-c is pressed
except KeyboardInterrupt:
	#Restore GPIO to default state
	GPIO.cleanup()