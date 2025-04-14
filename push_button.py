import RPi.GPIO as GPIO
import time

LED_PIN = 18
BUTTON_PIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        button_state = GPIO.input(BUTTON_PIN)
        GPIO.output(LED_PIN, not button_state)  # led is on only when button is pressed
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
