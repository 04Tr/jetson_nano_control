from control import Control
from operate_txt import Operate
from PCA9685 import PCA9685
from activate import Activate
import smbus
import time
import keyboard
import Jetson.GPIO as GPIO

min_time = 0.1
act = Activate()
class All_control:
    def __init__(self, run_time=min_time, path='data.txt'):
        self.control = Control()
        self.operate = Operate(path)
        self.run_time = run_time

    def clear_motor(self, serial, flag):
        self.control.set_direction(serial, flag)
        self.control.set_speed(serial, 0.8)
        time.sleep(self.run_time)

    def read_all_analog(self):
        self.control.select_channel(0)
        analog_value_0 = self.control.read_analog(0)
        analog_value_1 = self.control.read_analog(1)
        analog_value_2 = self.control.read_analog(2)
        print(f"通道 0 的模拟值为: {analog_value_0}")
        print(f"通道 0 的模拟值为: {analog_value_1}")
        print(f"通道 0 的模拟值为: {analog_value_2}")
        print("##===========================##")
        return analog_value_0, analog_value_1, analog_value_2

if __name__ == '__main__':
    con = All_control()
    try:
        while True:
            if keyboard.is_pressed('a'):
                con.control.select_channel(1)
                con.clear_motor(0, 0)
                con.control.set_speed(0, 0)
                ana_1, ana_2, ana_3 = con.read_all_analog()
            elif keyboard.is_pressed('s'):
                con.control.select_channel(1)
                con.clear_motor(0, 1)
                con.control.set_speed(0, 0)
                ana_1, ana_2, ana_3 = con.read_all_analog()
            elif keyboard.is_pressed('d'):
                con.control.select_channel(1)
                con.clear_motor(1, 0)
                con.control.set_speed(1, 0)
                ana_1, ana_2, ana_3 = con.read_all_analog()
            elif keyboard.is_pressed('f'):
                con.control.select_channel(1)
                con.clear_motor(1, 1)
                con.control.set_speed(1, 0)
                ana_1, ana_2, ana_3 = con.read_all_analog()
            elif keyboard.is_pressed('g'):
                con.control.select_channel(1)
                con.clear_motor(2, 0)
                con.control.set_speed(2, 0)
                ana_1, ana_2, ana_3 = con.read_all_analog()
            elif keyboard.is_pressed('h'):
                con.control.select_channel(1)
                con.clear_motor(2, 1)
                con.control.set_speed(2, 0)
                ana_1, ana_2, ana_3 = con.read_all_analog()
            elif keyboard.is_pressed('q'):
                con.control.select_channel(1)
                con.control.clear()
                break
    except KeyboardInterrupt:
        con.control.select_channel(1)
        con.control.clear()
        print("program over")