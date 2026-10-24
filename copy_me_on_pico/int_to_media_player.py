

import time
import board
import digitalio
import usb_hid

from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

class IntS2WToMediaPlayer:
  
    def __init__(self):
        self.control = ConsumerControl(usb_hid.devices)


    def int_to_control(self, value: int):
        # VolumeDown	174	0xAE	1174	2174
        if value == 1174:
             self.control.send(ConsumerControlCode. VOLUME_DECREMENT)
        # VolumeUp	175	0xAF	1175	2175
        elif value == 1175:
             self.control.send(ConsumerControlCode.VOLUME_INCREMENT)
        # VolumeMute	173	0xAD	1173	2173
        elif value == 1173:
             self.control.send(ConsumerControlCode.MUTE)
        # Play	250	0xFA	1250	2250
        elif value == 1250:
             self.control.send(ConsumerControlCode.PLAY_PAUSE)
        # MediaPlay	179	0xB3	1179	2179
        elif value == 1179:
             self.control.send(ConsumerControlCode.PLAY_PAUSE)
        # MediaNextTrack	176	0xB0	1176	2176
        elif value == 1176:
             self.control.send(ConsumerControlCode.SCAN_NEXT_TRACK)
        # MediaPreviousTrack	177	0xB1	1177	2177
        elif value == 1177:
             self.control.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK)
        # MediaStop	178	0xB2	1178	2178
        elif value == 1178:
             self.control.send(ConsumerControlCode.STOP)
        # RECORD = 0xB2
        elif value == 1321:
                self.control.send(ConsumerControlCode.RECORD)
        else:
            pass
        
    # FAST_FORWARD = 0xB3
    # REWIND = 0xB4
    # EJECT = 0xB8
    # BRIGHTNESS_DECREMENT = 0x70
    # https://github.com/adafruit/Adafruit_CircuitPython_HID/blob/main/adafruit_hid/consumer_control_code.py
    #     https://www.usb.org/sites/default/files/hut1_21_0.pdf#page=118.
