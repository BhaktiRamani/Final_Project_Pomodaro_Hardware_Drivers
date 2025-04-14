# Trying the simple eld blink program to get familiarized with python GPIO and RPi

import RPi.GPIO as GPIO
import time

LED_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)  # led on
        time.sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)   # led off
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
