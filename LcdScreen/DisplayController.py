import RPi.GPIO as GPIO
import RPLCD
from RPLCD import CharLCD

# Initialize display. All values have default values and are therefore
# optional.
lcd = CharLCD(pins_data=[35, 38, 37, 40])

try:
    lcd.write_string(u'I love you <3 !')
    input("Press any key")
finally:
    lcd.close(clear=True)
