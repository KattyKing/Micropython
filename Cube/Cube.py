from time import sleep
from machine import Pin
from neopixel import NeoPixel
import urandom


button_pin = Pin(5, Pin.IN)
strip_pin = Pin(2, Pin.OUT)

count_of_LED = 8
np = NeoPixel(strip_pin, count_of_LED)

def button_pressed():
	led_range = urandom.getrandbits(3) + 1
	for l_r in range(0, led_range):
		np[l_r] = (255, 255, 255)
	for l_r in range(led_range + 1, count_of_LED):
		np[l_r] = (0, 0, 0)
	np.write()
	sleep(1)

	
def button_released():
	for x in range(0, 8):
		np[x] = (0, 0, 0)
	np.write()


def cube():
	while True:
		if button_pin.value() == 0:
			button_pressed()
		elif button_pin.value() == 1:
			button_released()

			
cube()
