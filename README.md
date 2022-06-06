# FP_IoT

Write : `MMM1AOYKATVN5EY6`

Read : `1ODO66IP53KDBYFC`

Channel ID : 1759134

Rain Module
```
DO - GPIO 17
VCC - 3V3 (1)
GND - GND (9)
```

DHT11
```
GND - GND (6)
DATA - GPIO 23
VCC - 3V3 (17)
```

Sound Sensor
```
DO - GPIO 18
GND - GND (39)
VCC - 5V (2)
```

```
sudo apt-get install python
sudo apt update
sudo apt full-upgrade
sudo apt install python3-pip
sudo pip3 install --upgrade setuptools
sudo reboot

sudo pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo python3 raspi-blinka.py

pip3 install adafruit-circuitpython-dht
sudo apt-get install libgpiod2

sudo apt-get install httplib
sudo apt-get install urllib
```
https://tinoiot.com/tutorials/thingspeak-bme280-raspberry-pi#setting-up-thingsspeak
https://docs.google.com/document/d/1JUn1DyAo0rIstE9gkYLCh-OdrywajCd9W-EOd_6dzSY/edit
