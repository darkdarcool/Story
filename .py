import os,random
import time, sys


#colors

black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bblack = "\033[0;90m"
bred = "\033[0;91m"
bgreen = "\033[0;92m"
byellow = "\033[0;93m"
bblue = "\033[0;94m"
bmagenta = "\033[0;95m"
bcyan = "\033[0;96m"
bwhite = "\033[0;97m"


message = (bgreen + "LOADING\n")

massage = message * 10 
print(message)
os.system('clear')
def typewriter(message):
	for i in message:
		sys.stdout.write(i)
		sys.stdout.flush()
		if ((i != "\n") and (i != ":")):
			time.sleep(0.9)
		else:
			time.sleep(0.9)

typewriter(red + 'THE END')
time.sleep(2)
os.system('clear')
os.system('clear')
def typewriter(message):
	for i in message:
		sys.stdout.write(i)
		sys.stdout.flush()
		if ((i != "\n") and (i != ":")):
			time.sleep(0.08)
		else:
			time.sleep(0.2)


			
typewriter('VROOM, you here the sound of the bus. Your just playing video games on your phone. PEW, PEW, PEW. Then you hear a sudden thud. But that was normal  ')



