import time
import traceback

import RPi.GPIO as GPIO


class DoorSensor(object):

    def __init__(self):
        self.input_channel = 11
        self.time_stamp = time.time()
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.input_channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def listen_to_edge(self):
        channel = GPIO.wait_for_edge(self.input_channel, GPIO.FALLING)
        print(channel)

if __name__ == '__main__':
    try:
        door_sensor = DoorSensor()
        door_sensor.listen_to_edge()
        input('Press any key to exit...')
    except Exception as e:
        print('An exception has occurred: {}'.format(e))
        traceback.print_exc()
    finally:
        GPIO.cleanup()
