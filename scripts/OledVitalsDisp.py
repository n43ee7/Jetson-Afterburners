#
# I2C Oled Display System Vitals Display code
# Optomised from NVIDIA Jetbot and Adafruit SSDXXX Libraries for lesser RAM consumption
#
# Nabeel Nayyar 11/15/2019 12:38 PM
#

import time

import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import pkg_resources
import platform
import os

import subprocess

def get_ip_address(interface):
    if get_network_interface_state(interface) == 'down':
        return None
    cmd = "ifconfig %s | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'" % interface
    return subprocess.check_output(cmd, shell=True).decode('ascii')[:-1]

def get_network_interface_state(interface):
    return subprocess.check_output('cat /sys/class/net/%s/operstate' % interface, shell=True).decode('ascii')[:-1]

oled = Adafruit_SSD1306.SSD1306_128_64(rst=None, i2c_bus=1, gpio=1) # setting gpio to 1 is hack to avoid platform detection
oled.begin()
oled.clear()
oled.display()
draw.rectangle((0,0,width,height), outline=0, fill=0)

padding = -2
top = padding
bottom = height-padding
x = 0

font = ImageFont.load_default()


while True:
    cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
    CPU = subprocess.check_output(cmd, shell = True )
    cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
    MemUsage = subprocess.check_output(cmd, shell = True )
    cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
    Disk = subprocess.check_output(cmd, shell = True )

    draw.text((x, top),       "NVIDIA JETSON NANO", font=font, fill=255)
    draw.text((x, top+8),     "==================================================", font=font, fill=255)
    draw.text((x, top+16),    "eth0: " + str(get_ip_address('eth0')),  font=font, fill=180)
    draw.text((x, top+25),    "wlan0: " + str(get_ip_address('wlan0')), font=font, fill=180)
    draw.text((x, top+34),    str(MemUsage.decode('utf-8')),  font=font, fill=180)
    draw.text((x, top+43),    str(Disk.decode('utf-8')),  font=font, fill=180)
    # ADD GPU USAGE PERCENTAGE
    draw.text((x, top+52),    "=================================================", font=font, fil=255)

    oled.image(image)
    oled.display()
    time.sleep(1)
