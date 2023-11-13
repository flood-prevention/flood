import time
from flask import Flask, request, render_template, jsonify
import RPi.GPIO as gpio
import MariaDB

app = Flask(__name__)
store = MariaDB.MariaDB()


pin1 = 16
pin2 = 18

gpio.setmode(gpio.BOARD)
gpio.setup(pin2, gpio.IN)
gpio.setup(pin1, gpio.OUT)
servo = gpio.PWM(pin1, 50)


def water():
    level_data = gpio.input(pin2)
    print(level_data)
    time.sleep(0.5)


@app.route("/")
def home():
    return render_template("index.html")


def setAngle(angle):
    duty = 2.5+10*angle/180
    print("degree : {} to {}(duty)".format(angle, duty))
    servo.ChangeDutyCycle(duty)


if __name__ == "__main__":
    servo.start(0)
    app.run(host="0.0.0.0")
    servo.stop()
