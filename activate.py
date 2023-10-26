import smbus
from PCA9685 import PCA9685

class Activate:
    def __init__(self):
        try:
            bus = smbus.SMBus(1)
            pwm = PCA9685(0x40, bus, debug=False)
        except:
            print("error")