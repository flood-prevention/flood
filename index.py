import time
from flask import Flask, request, render_template, jsonify
import RPi.GPIO as gpio
import MariaDB

app = Flask(__name__)
store = MariaDB.MariaDB()

pin1 = 12
pin2 = 16
pin3 = 18
pin4 = 22

gpio.setmode(gpio.BOARD)
gpio.setup(pin4, gpio.IN)
gpio.setup(pin3, gpio.IN)
gpio.setup(pin1, gpio.OUT)
gpio.setup(pin2, gpio.OUT)
servo1 = gpio.PWM(pin1, 50)
servo2 = gpio.PWM(pin2, 50)


def water_1():
    level_data_1 = gpio.input(pin3)
    print(level_data_1)
    time.sleep(0.5)
    return level_data_1


def water_2():
    level_data_2 = gpio.input(pin4)
    print(level_data_2)
    time.sleep(0.5)
    return level_data_2


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/water_level')
def water_level_1():
    level_1 = water_1()
    level_2 = water_2()
    result = store.add(level_1, level_2)
    return result


@app.route('/water_level/open_1')
def open_1():
    return setAngle_1(90)


@app.route('/water_level/close_1')
def close_1():
    return setAngle_1(0)


@app.route('/water_level/open_2')
def open_2():
    return setAngle_2(90)


@app.route('/water_level/close_2')
def close_2():
    return setAngle_2(0)


def setAngle_1(angle):
    duty = 2.5+10*angle/180
    print("degree : {} to {}(duty)".format(angle, duty))
    servo1.ChangeDutyCycle(duty)


def setAngle_2(angle):
    duty = 2.5+10*angle/180
    print("degree : {} to {}(duty)".format(angle, duty))
    servo2.ChangeDutyCycle(duty)


if __name__ == "__main__":
    servo1.start(0)
    servo2.start(0)
    app.run(host="0.0.0.0")
    servo1.stop()
    servo2.stop()
