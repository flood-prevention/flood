from flask import Flask, request, render_template, jsonify
import RPi.GPIO as gpio
from time

pin1 = 16
pin2 = 18

def water()

gpio.setmode(gpio.BOARD)
gpio.setup(pin1, gpio.OUT)
gpio.setup(pin2, gpio.IN)
servo = gpio.PWM(pin1, 50)

@app.route("/")
def home():
    return render_template("")


def setAngle(angle):
    duty = 2.5+10*angle/180
    print("degree : {} to {}(duty)".format(angle, duty))
    servo.ChangeDutyCycle(duty)


if __name__=="__main__":
    servo.start(0)
    app.run(host="0.0.0.0")
    servo.stop()