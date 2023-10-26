import smbus
import time
from PCA9685 import PCA9685
import Jetson.GPIO as GPIO
from control import Control
import keyboard

min_time = 0.1

class Recover:
    def __init__(self):
        self.recover = Control()

    def clear_motor(self, serial, flag):
        self.recover.set_direction(serial, flag)
        self.recover.set_speed(serial, 0.8)
        time.sleep(min_time)

if __name__=="__main__":
    rec = Recover()
    rec.recover.select_channel(1)
    while True:
        if keyboard.is_pressed('a'):
            rec.clear_motor(0, 0)
            rec.recover.set_speed(0, 0)     # 模拟量读取放到每个if后
        elif keyboard.is_pressed('s'):
            rec.clear_motor(0, 1)
            rec.recover.set_speed(0, 0)
        elif keyboard.is_pressed('d'):
            rec.clear_motor(1, 0)
            rec.recover.set_speed(1, 0)
        elif keyboard.is_pressed('f'):
            rec.clear_motor(1, 1)
            rec.recover.set_speed(1, 0)
        elif keyboard.is_pressed('g'):
            rec.clear_motor(2, 0)
            rec.recover.set_speed(2, 0)
        elif keyboard.is_pressed('h'):
            rec.clear_motor(2, 1)
            rec.recover.set_speed(2, 0)
        elif keyboard.is_pressed('q'):
            rec.recover.clear()
            break