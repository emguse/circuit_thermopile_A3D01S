import board
import busio
import time
from adafruit_bus_device.i2c_device import I2CDevice

'''
- Applicable to Nippon Ceramic's thermopile sensor 'A3D01S-FU-50-60'
- 2022/01/25 ver.1.10
- Author : emguse
- License: MIT License
'''

I2C_ADDRES = 0x3D

class ThermopileInfraredSensorA3D01S_FU_50_60():
    def __init__(self, i2c) -> None:
        time.sleep(0.05)
        self.a3d01s_addres = I2C_ADDRES
        self.device = I2CDevice(i2c, self.a3d01s_addres)
        self.self_temp = 0
        self.object_temp = 0
    def self_temperature(self):
        with self.device:
            read_addres = bytes([0x70])
            raw = bytearray(3)
            self.device.write_then_readinto(read_addres, raw)
            pv = (raw[0] | raw[1] << 8)
            self.self_temp = pv / 8 - 20 # Celsius degree
    def object_temperature(self):
        with self.device:
            read_addres = bytes([0x71])
            raw = bytearray(3)
            self.device.write_then_readinto(read_addres, raw)
            pv = (raw[0] | raw[1] << 8)
            self.object_temp = pv / 8 - 30 # Celsius degree

def main(): 
    I2C_SCL = board.SCL
    I2C_SDA = board.SDA  
    i2c = busio.I2C(scl=I2C_SCL, sda=I2C_SDA)
    
    a3d01s = ThermopileInfraredSensorA3D01S_FU_50_60(i2c)
    
    while True:
        a3d01s.self_temperature()
        a3d01s.object_temperature()
        print("self_temp  : ", str(a3d01s.self_temp))
        print("object_temp: ", str(a3d01s.object_temp))
        time.sleep(0.5)

if __name__ == "__main__":
    main()