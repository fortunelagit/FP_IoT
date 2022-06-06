import board, busio, adafruit_dht
import requests
import sched, time
import psutil
import RPi.GPIO as GPIO
from gpiozero import InputDevice

for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()

sensor = adafruit_dht.DHT11(board.D23)

channel = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

no_rain = InputDevice(17)

s = sched.scheduler(time.time, time.sleep)
interval = 5


def read_and_send(sc): 

    queries = {"api_key": "MMM1AOYKATVN5EY6",
               "field2": round(sensor.humidity, 2), 
               "field3": round(sensor.temperature, 2),
               "field5": GPIO.input(channel)}

    r = requests.get('https://api.thingspeak.com/update', params=queries)

    if r.status_code == requests.codes.ok:
        print("Data Received!")
    else:
        print("Error Code: " + str(r.status_code))

    s.enter(interval, 1, read_and_send, (sc,))

def callback(channel):
        if GPIO.input(channel):
                queries = {"api_key": "MMM1AOYKATVN5EY6",
                           "field5": 1}
        else:
                queries = {"api_key": "MMM1AOYKATVN5EY6",
                           "field5": 0}             

        r = requests.get('https://api.thingspeak.com/update', params=queries)

        if r.status_code == requests.codes.ok:
            print("Sound Received!")
        else:
            print("Error Code: " + str(r.status_code))

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)

while True:
    if not no_rain.is_active:
        print("It's raining!")
    else:
        print("The rain has stopped.")
    sleep(1)

s.enter(interval, 1, read_and_send, (s,))
s.run()
