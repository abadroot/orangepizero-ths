#!/usr/bin/env python
#
# !!! Needs psutil (+ dependencies) installing:
#
#    $ sudo apt-get install python-dev
#    $ sudo pip install psutil
#

#from datetime import datetime
from oled.device import ssd1306, sh1106
from oled.render import canvas
from PIL import ImageFont

#
from pyA20.gpio import gpio
from pyA20.gpio import port
import dht11

#
import time

# initialize GPIO
PIN2 = port.PA6
gpio.init()
# read data using pin 14
instance = dht11.DHT11(pin=PIN2)

def main():
    oled = ssd1306(port=0, address=0x3C)
    font = ImageFont.load_default()
    font2 = ImageFont.truetype('./FreeSans.ttf', 20)

    c = 0
    t_ok = 0
    h_ok = 0

    while True:
        result = instance.read()

        if result.is_valid():
            t_ok = result.temperature
            h_ok = result.humidity
            str_status = "."
        else:
            str_status = "o"

        if c <= 0:
            c = 10 
        else:
            c = c - 1

        with canvas(oled) as draw:
                draw.text((0,0), "Temp: %d C" % t_ok, font=font2, fill=255)
                draw.text((0,40), "Um: %d %%    %s" % (h_ok,str_status), font=font2, fill=255)

        # debug
        #print(str_status)
        #print(c)
        #print("%d - %d" % (t_ok,h_ok))

        time.sleep(1)

if __name__ == "__main__":
    main()
