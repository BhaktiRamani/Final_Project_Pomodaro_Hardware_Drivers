import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 1000)

def play_tone(freq, duration):
    pwm.ChangeFrequency(freq)
    pwm.start(50)
    time.sleep(duration)
    pwm.stop()
    time.sleep(0.05)
    
    
def system_end():
    #otes = [343, 299, 200]
    #notes = [783, 659, 523]
    #notes = [783, 659, 523, 392, 349, 293, 261]
    notes = [783.99, 659.25, 587.33, 523.25, 493.88, 392.00]
    duration = [0.15, 0.15, 0.15, 0.2, 0.3]
    for notes, duration in zip(notes, duration):
        play_tone(notes, duration)
    
    
def system_start():
    notes = [392, 523.25, 587.33, 659.25, 523.25]
    duration = [0.15, 0.15, 0.15, 0.2, 0.3]
    for notes, duration in zip(notes, duration):
        play_tone(notes, duration)
        
def pomodaro_start():
    notes = [523.25, 587.33, 659.25, 698.46, 783.99, 880.00]
    duration = [0.1, 0.1, 0.1, 0.1, 0.15, 0.2]
    for notes, duration in zip(notes, duration):
        play_tone(notes, duration)
        
        
def pomodaro_end():
    notes = [ 880.00, 783.99, 659.25, 587.33, 659.25, 523.25]
    duration = [0.1, 0.1, 0.1, 0.1, 0.15, 0.2]
    for notes, duration in zip(notes, duration):
        play_tone(notes, duration)
        
def pomodaro_ambient():
    notes = [98.00, 123.47, 146.83, 130.81]
    duration = [0.7, 0.7, 0.8, 1.0]
    for notes, duration in zip(notes, duration):
        play_tone(notes, duration)
        time.sleep(0.3)
    
        

        
try:
    for i in range(2):
        print("start of the system playing")
        system_start()
        time.sleep(2)
        print("Pomodaro start playing")
        pomodaro_start()
        time.sleep(2)
        print("Pomodaro ambient playing")
        pomodaro_ambient()
        time.sleep(2)
        print("Pomodaro end playing")
        pomodaro_end()
        time.sleep(2)
        print("end of the playing")
        system_end()
        time.sleep(1)

    
finally:
    pwm.stop()
    GPIO.cleanup()