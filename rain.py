# raindrop sensor DO connected to GPIO18
# HIGH = no rain, LOW = rain detected
# Buzzer on GPIO13
from time import sleep
from gpiozero import InputDevice

no_rain = InputDevice(17)
 
while True:
    if not no_rain.is_active:
        print("It's raining!")
    else:
        print("The rain has stopped.")
        # insert your other code or functions here
        # e.g. tweet, SMS, email, take a photo etc.
    sleep(1)