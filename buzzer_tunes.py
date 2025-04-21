import RPi.GPIO as GPIO
import time

# the pin connected to the buzzer
BUZZER_PIN = 18

# GPIO Congiguration
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# Setting up PWM on the buzzer pin at 1kHz
pwm = GPIO.PWM(BUZZER_PIN, 1000)  # Start frequency = 1000 Hz

def play_tone(frequency, duration):
    pwm.ChangeFrequency(frequency)
    pwm.start(50)  # 50% duty cycle
    time.sleep(duration)
    pwm.stop()
    time.sleep(0.05)  # Small pause  

def play_tune_1():
    # Simplple low to high tune
    notes = [262, 294, 330, 349, 392, 440, 494, 523]  # C4 to C5
    for note in notes:
        play_tone(note, 0.2)

def play_tune_2():
    # Twinkle Twinkle (first part)
    melody = [(262, 0.4), (262, 0.4), (392, 0.4), (392, 0.4),
              (440, 0.4), (440, 0.4), (392, 0.8)]
    for note, duration in melody:
        play_tone(note, duration)

def play_tune_3():
    # random pattern
    melody = [(392, 0.2), (349, 0.2), (330, 0.3), (294, 0.3), (262, 0.5)]
    for note, duration in melody:
        play_tone(note, duration)

try:
    print("Playing Tune 1")
    play_tune_1()
    time.sleep(1)

    print("Playing Tune 2")
    play_tune_2()
    time.sleep(1)

    print("Playing Tune 3")
    play_tune_3()

finally:
    pwm.stop()
    GPIO.cleanup()

