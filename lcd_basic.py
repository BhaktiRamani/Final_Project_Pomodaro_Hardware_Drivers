#!/usr/bin/python3

from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
import time
import datetime
import RPi.GPIO as GPIO

lcd = LCD()

BUTTON_PIN = 23  # Connect the push button here
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def safe_exit(signum, frame):
    lcd.clear()
    exit(1)

signal(SIGTERM, safe_exit)
signal(SIGHUP, safe_exit)

def scroll_text(text, line, delay=0.3, width=16):
    for i in range(len(text) - width + 1):
        lcd.text(text[i:i+width], line)
        time.sleep(delay)

try:
    lcd.text("Hello", 1)
    lcd.text("Bhakti Ramani", 2)
    time.sleep(2)

    lcd.clear()
    scroll_text("AESD", 1)
    time.sleep(1)

    while True:
        # Print date
        now = datetime.datetime.now().strftime("%H:%M:%S")
        lcd.text("Time: " + now, 1)
        lcd.text("Press the button...", 2)

        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            lcd.text("Button Pressed!", 2)
            time.sleep(1)

        time.sleep(0.5)

except KeyboardInterrupt:
    pass
finally:
    lcd.clear()
    GPIO.cleanup()
