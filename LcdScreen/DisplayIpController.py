import netifaces
import time
from subprocess import Popen, PIPE
from RPLCD import CharLCD


def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

if __name__ == '__main__':
    lcd = CharLCD(pin_rs=37, pin_e=40, pin_rw=None, pins_data=[38, 35, 36, 33], cols=16, rows=2)

    try:
        while True:
            for interface in netifaces.interfaces():
                addresses = netifaces.ifaddresses(interface)
                if netifaces.AF_INET in addresses:
                    family = addresses[netifaces.AF_INET]
                    for idx, address_attrs in enumerate(family):
                        lcd.clear()
                        lcd.write_string('{}'.format(interface))
                        lcd.cursor_pos = (1, 0)
                        lcd.write_string(address_attrs['addr'])
                        time.sleep(4)
    finally:
        lcd.close(clear=True)
