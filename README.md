# circuit_thermopile_A3D01S
This repository contains hardware and software for a non-contact thermometer module using a thermopile sensor.

# Notes
- The main thermopile sensor can be ordered through mail order in Japan. Or you will have to go to Akihabara to get it.
- You will need to be equipped with a hot plate or oven that can be surface mounted.

# Features

- Wide range of non-contact temperature measurement from 30°C to 400°C
- Easy connection with STEMMA/QT, Qwiic compatible connector (JST SH)
- Built-in 5V voltage booster circuit
- Built-in I2C signal level conversion circuit
- CircuitPython program available

# What you need

- PB-0011-A
- Parts on PB-0011-A -> PB-0011-A.csv
- A3D01S-FU-50-60 : thermopile sensor 'A3D01S-FU-50-60' [Nippon Ceramic](https://www.nicera.co.jp/en/) 
- [Where to buy thermopile sensor](https://akizukidenshi.com/catalog/g/gI-16059/)

# Requirement
- adafruit_bus_device.i2c_device
- adafruit_register
- adafruit_pypixelbuf
- neopixel

# Author

- Author: emguse