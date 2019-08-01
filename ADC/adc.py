from machine import Pin, ADC
from time import sleep

LDR = ADC(0)
pin_diode = Pin(4, Pin.OUT)
pin_second_diode = Pin(2, Pin.OUT)

def read_value():
	pot_value = LDR.read()
	return pot_value	
	
def blink(pot_value):
	if pot_value < 900:
		pin_diode.value(1)
		pin_second_diode.value(0)
	
	else:
		pin_diode.value(0)
		pin_second_diode.value(1)
	
def loop():
	while True:
		ldr_value = read_value()
		blink(ldr_value)
		sleep(0.1)
		
loop()
		
