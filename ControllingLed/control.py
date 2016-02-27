import time
import traceback

import RPi.GPIO as GPIO


class LedController(object):

    def __init__(self):
        self.input_channel = 11
        self.red_output_channel = 12
        self.green_output_channel = 16
        self.time_stamp = time.time()
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.red_output_channel, GPIO.OUT)
        GPIO.setup(self.green_output_channel, GPIO.OUT)
        GPIO.setup(self.input_channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.output(self.green_output_channel, GPIO.LOW)

    def listen_to_edge(self):
        GPIO.add_event_detect(self.input_channel, GPIO.BOTH, callback=self.red_event_detected)

    def red_event_detected(self, channel):
        time_now = time.time()
        input_state = GPIO.input(self.input_channel)
        if time_now - self.time_stamp > 0.3:
            green_output_state = GPIO.input(self.green_output_channel)
            if input_state == GPIO.HIGH:
                GPIO.output(self.green_output_channel, not green_output_state)

        self.time_stamp = time_now
        GPIO.output(self.red_output_channel, input_state)


if __name__ == '__main__':
    try:
        led_controller = LedController()
        led_controller.listen_to_edge()
        input('Press any key to exit...')
    except Exception as e:
        print('An exception has occurred: {}'.format(e))
        traceback.print_exc()
    finally:
        GPIO.cleanup()
