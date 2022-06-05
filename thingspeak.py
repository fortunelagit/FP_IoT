import time
import RPi.GPIO as GPIO
import sys
import urllib2

def getSensorData():
    GPIO.setmode(GPIO.BOARD)

    trig = 38
    echo = 40
    GPIO.setwarnings(False)
    GPIO.setup(echo, GPIO.IN)
    GPIO.setup(trig, GPIO.OUT)

    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    while GPIO.input(echo) == 0: pass
    
    start = time.time()

    while GPIO.input(echo) == 1:  pass

    end = time.time()

    distance = ((end - start) * 34300) / 2

    return (int (distance))


def main():
    key = '56NF826GVDYTQHPT'
    baseURL = 'https://api.thingspeak.com/update?api_key=%s' % key
       
    while True:
        try:
            distance = getSensorData()
            f = urllib2.urlopen(baseURL + "&field1=%s" % int(distance/5))
            print f.read()
            f.close()
            sleep(15)
        except:
            print 'exiting.'
            break

           
if __name__ == '__main__':
    main()            