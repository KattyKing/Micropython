# ADC pin: Analog-to-digital converter on NodeMCU

## What does this circuit do?

On one side there is simple light sensor made from photoresistor (LDR), its resistivity depends on light. 
On the second side lays two LEDs. 
When the LDR is in the dark, blue LED will light up; when LDR in light is, than the green LED light up.

![alt text](https://github.com/KattyKing/Micropython/blob/master/ADC/picture/ldr.jpg)

## How it works?

LDR and second resistor create a voltage divider. Voltage distribution is changing due to change of LDR resistivity. 
Pin A0 is reading the voltage value on LDR (0-3.3 V) and converts it into value between 0-1023. So when resistivity of both reistors is the same,  the value on A0 will be 512.
Based on this input value it is posible to control some output. In this example it is controling choice of LED.

![alt text](https://github.com/KattyKing/Micropython/blob/master/ADC/picture/ldr_scheme.png)

https://en.wikipedia.org/wiki/Analog-to-digital_converter

https://randomnerdtutorials.com/esp32-esp8266-analog-readings-micropython/

