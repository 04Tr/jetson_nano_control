import smbus
import time
from PCA9685 import PCA9685
import Jetson.GPIO as GPIO

# 初始化参数
IN1 = 11
IN2 = 13
IN3 = 19
IN4 = 21
IN5 = 29
IN6 = 31
INPUT_1 = [IN1, IN2]
INPUT_2 = [IN3, IN4]
INPUT_3 = [IN5, IN6]
INPUTS = [IN1, IN2, IN3, IN4, IN5, IN6]

# TCA9548A 的 I2C 地址
tca9548a_address = 0x70

# PCF8591 的 I2C 地址
pcf8591_address = 0x48

# PCA9685 的 I2C 地址
pca9685_address = 0x40

class Control:
    def __init__(self, channels=INPUTS):
        GPIO.setmode(GPIO.BOARD)                             # 设置GPIO模式为BOARD
        GPIO.setup(channels, GPIO.OUT)                       # 将传入管脚设置为输出
        self.bus = smbus.SMBus(1)                            # 1 表示使用 /dev/i2c-1
        self.freq = 1000                                     # PWM波频率设置
        self.pwm = PCA9685(pca9685_address, self.bus, debug=False)     # 创建PWM波控制对象
        self.pwm.setPWMFreq(self.freq)                       # 设置PWM波频率
        self.channels = channels

    # 通过tca选择i2c通道
    def select_channel(self, channel):
        self.bus.write_byte(tca9548a_address, 0x01 | channel)

    # 读取模拟值
    def read_analog(self, channel):   # channel = 0, 1, 2, 3，选择pcf模拟输入
        self.bus.write_byte(pcf8591_address, 0x40 | channel)  # 设置单端输入模式
        self.bus.read_byte(pcf8591_address)     # 清除上一步转换结果，保证数据准确
        analog_value = self.bus.read_byte(pcf8591_address)
        return analog_value

    # 调控速度
    def set_speed(self, channel, duty):                     # channel为pca输出pwm的管脚编号
        off_set = int(self.freq * 4 * duty)                 # 根据占空比计算off值,on值默认为0
        self.pwm.setPWM(channel, 0, off_set)

    # 控制转向
    def set_direction(self, serial, flag):                # serial为电机编号0,1,2，flag为0表示正转，1为反转
        number = serial * 2
        if flag == 0:
            GPIO.output(self.channels[number], GPIO.HIGH)
            GPIO.output(self.channels[number + 1], GPIO.LOW)
        elif flag == 1:
            GPIO.output(self.channels[number], GPIO.LOW)
            GPIO.output(self.channels[number + 1], GPIO.HIGH)
        else:
            print("请正确输入")

    # 恢复初始状态
    def clear(self):
        GPIO.cleanup()
        # 状态清理，确保代码停止运行时电机停止转动
        for i in range(3):
            self.set_speed(i, 0)
            self.pwm.setPWM(i, 0, 0)

if __name__ == "__main__":
    control = Control()
    try:
        while True:
            # 选择tca通道0作为传感器通道
            control.select_channel(0)
            analog_value_0 = control.read_analog(0)
            print(f"通道 0 的模拟值为: {analog_value_0}")
            analog_value_1 = control.read_analog(1)
            print(f"通道 0 的模拟值为: {analog_value_1}")
            analog_value_2 = control.read_analog(2)
            print(f"通道 0 的模拟值为: {analog_value_2}")
            print("##===========================##")

            # 选择tca通道1作为电机控制通道
            control.select_channel(1)
            # 控制三个电机转动
            control.set_direction(0, 0)
            control.set_speed(0, 0.8)
            control.set_direction(1, 0)
            control.set_speed(1, 0.8)
            control.set_direction(2, 0)
            control.set_speed(2, 0.8)
            time.sleep(0.2)

    except KeyboardInterrupt:
        control.select_channel(1)
        control.clear()
        print("测试结束")
