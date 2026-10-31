

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
        #print(f"Media Player Received value: {value}")
        # VolumeDown	174	0xAE	1174	2174
        if value == 1174:
             self.control.send(ConsumerControlCode. VOLUME_DECREMENT)
             #print("Volume Down ✅")
             #print("U")
        # VolumeUp	175	0xAF	1175	2175
        elif value == 1175:
             self.control.send(ConsumerControlCode.VOLUME_INCREMENT)
             #print("Volume Up ✅")
             #print("D")
        # VolumeMute	173	0xAD	1173	2173
        elif value == 1173:
             self.control.send(ConsumerControlCode.MUTE)
             print("Mute ✅")
        # Play	250	0xFA	1250	2250
        elif value == 1250:
             self.control.send(ConsumerControlCode.PLAY_PAUSE)
             print("Play/Pause")
        # MediaPlay	179	0xB3	1179	2179
        elif value == 1179:
             self.control.send(ConsumerControlCode.PLAY_PAUSE)
             print("Play/Pause")
        # MediaNextTrack	176	0xB0	1176	2176
        elif value == 1176:
             self.control.send(ConsumerControlCode.SCAN_NEXT_TRACK)
             print("Next Track")
        # MediaPreviousTrack	177	0xB1	1177	2177
        elif value == 1177:
             self.control.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK)
             print("Previous Track")
        # MediaStop	178	0xB2	1178	2178
        elif value == 1178:
             self.control.send(ConsumerControlCode.STOP)
             print("Stop")
        # RECORD = 0xB2
        elif value == 1321:
                self.control.send(ConsumerControlCode.RECORD)
                print("Record")
        else:
            pass
        
    # FAST_FORWARD = 0xB3
    # REWIND = 0xB4
    # EJECT = 0xB8
    # BRIGHTNESS_DECREMENT = 0x70
    # https://github.com/adafruit/Adafruit_CircuitPython_HID/blob/main/adafruit_hid/consumer_control_code.py
    #     https://www.usb.org/sites/default/files/hut1_21_0.pdf#page=118.
