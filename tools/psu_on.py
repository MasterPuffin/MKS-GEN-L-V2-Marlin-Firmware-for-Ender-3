import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

GPIO.output(14, GPIO.LOW)
GPIO.output(15, GPIO.LOW)

