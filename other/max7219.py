
import sys
sys.path.append('/usr/src/python/SAKS20')

from sakspins import SAKSPins as PINS
import RPi.GPIO as GPIO
import time


PIN_DIN = PINS.BCM001
PIN_CS = PINS.BCM002
PIN_CLK = PINS.BCM003


def setByte(byteData):
	for bit in range(0, 8):
		if ((byteData<<bit) & 0x80 == 0x80):
			setBitData(GPIO.HIGH)
		else:
			setBitData(GPIO.LOW)

def delay():
	pass
	# time.sleep(0.001)

def setBitData(data):
	# print(str(data) + ' ')
	delay()
	GPIO.output(PIN_CLK, GPIO.LOW)
	delay()
	GPIO.output(PIN_DIN, data)
	delay()
	GPIO.output(PIN_CLK, GPIO.HIGH)
	delay()

def setShutdownMode(mode = 1):
	GPIO.output(PIN_CS, GPIO.LOW)

	setByte(0x09)
	
	if (mode == 1) :
		setByte(0x00)
	elif (mode == 2) :
		setByte(0x01)
	elif (mode == 3) :
		setByte(0x0f)
	elif (mode == 4) :
		setByte(0xff)

	GPIO.output(PIN_CS, GPIO.HIGH)


def setShutdownMode(mode = 1):
	GPIO.output(PIN_CS, GPIO.LOW)

	setByte(0x09)
	
	if (mode == 1) :
		setByte(0x00)
	elif (mode == 2) :
		setByte(0x01)
	elif (mode == 3) :
		setByte(0x0f)
	elif (mode == 4) :
		setByte(0xff)

	GPIO.output(PIN_CS, GPIO.HIGH)

def setDecodeMode(mode = 4):
	GPIO.output(PIN_CS, GPIO.LOW)

	setByte(0x09)
	
	if (mode == 1) :
		setByte(0x00)
	elif (mode == 2) :
		setByte(0x01)
	elif (mode == 3) :
		setByte(0x0f)
	elif (mode == 4) :
		setByte(0xff)

	GPIO.output(PIN_CS, GPIO.HIGH)

def setIntensity(mode = 8):
	GPIO.output(PIN_CS, GPIO.LOW)

	setByte(0x0A)
	setByte(mode)

	GPIO.output(PIN_CS, GPIO.HIGH)


def setScanLimit(mode = 7):
	GPIO.output(PIN_CS, GPIO.LOW)

	setByte(0x0B)
	
	setByte(mode)

	GPIO.output(PIN_CS, GPIO.HIGH)


def setDisplayTestMode(mode = 0):
	GPIO.output(PIN_CS, GPIO.LOW)

	setByte(0x0f)
	
	setByte(mode)

	GPIO.output(PIN_CS, GPIO.HIGH)



def write():
	n=0
	while True:
		print(n)
		n=n+1
		showDigit(1, int(n)%10, False)
		showDigit(2, int(n/10)%10, False)
		showDigit(3, int(n/100)%10, False)
		showDigit(4, int(n/1000)%10, False)
		showDigit(5, int(n/10000)%10, False)
		showDigit(6, int(n/100000)%10, False)
		showDigit(7, int(n/1000000)%10, False)
		showDigit(8, int(n/10000000)%10, False)
		time.sleep(0.01)

def showDigit(no, num, showDotPoint):
	GPIO.output(PIN_CS, GPIO.LOW)
	setByte(no)
	if (showDotPoint):
		setByte(num | 0x80)
	else:
		setByte(num)

	GPIO.output(PIN_CS, GPIO.HIGH)

def test():
	setShutdownMode()
	setDecodeMode()
	setIntensity(1)
	setScanLimit()
	setDisplayTestMode()

	write()


def init():
	# GPIO.setwarnings(False)
	# 
	GPIO.setmode(GPIO.BCM)
	
	GPIO.setup(PIN_DIN, GPIO.OUT)
	GPIO.setup(PIN_CS, GPIO.OUT)
	GPIO.setup(PIN_CLK, GPIO.OUT)
	pass


def exit():
	GPIO.cleanup()

def main():
	init()
	
	try:
		test()
	except KeyboardInterrupt:
		pass

	exit()



if __name__ == '__main__':
	main()


