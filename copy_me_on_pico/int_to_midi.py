# In CircuitPython, this module converts integer values to MIDI note numbers.

"""

Full Midi
Explanation of MIDI Format Tags

MIDI data is stored using 3 bytes, but I use 4-byte tags to make it more recognizable.

Tagging an event with 13 indicates that the following data is in MIDI format:
1300000000

For simplicity, here’s a beginner-friendly reference using values 0–127 in the tag system:

1600 – Play full note 0 | 2600 – Release note 0
1727 – Play full note 127 | 2727 – Release note 127
1728 – Press all notes | 2728 – Release all notes
In tribute to Mordhau:

1729 – Switch to Flute | 2729 – Switch to Muse
1730 – Play note 0
1790 – Play note 60
Note: Mordhau mode does not use note releases.
"""


import usb_midi
import adafruit_midi
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff

class IntS2WToMidi:
    def __init__(self):
        # prepare the midi output on circuit python
        self.midi = adafruit_midi.MIDI(
            midi_out=usb_midi.ports[1], 
            out_channel=0
        )
    def int_to_midi(self, int_value):
        bool_is_valide_1000 = (int_value>=1600 and int_value < 1600 + 128) or (int_value>=2600 and int_value < 2600 + 128)
        bool_is_valide_as_tag_13 = int(int_value / 100000000) % 100 == 13

        if not bool_is_valide_1000 and not bool_is_valide_as_tag_13:
            return  # Not a valid MIDI command

        if bool_is_valide_1000:
            bool_pression = int_value < 2000
            if bool_pression:            # Note On
                value = int_value - 1600
                value = min(max(value, 0), 127)  # Clamp value between 0 and 127
                self.midi.send(NoteOn(value, 127))
            else:                        # Note Off
                value = int_value - 2600
                value = min(max(value, 0), 127)  # Clamp value between 0 and 127
                self.midi.send(NoteOff(value, 0))
                
        elif bool_is_valide_as_tag_13:
            four_byte_of_int = ((int_value >> 24) & 0xFF,
                                (int_value >> 16) & 0xFF,
                                (int_value >> 8) & 0xFF,
                                int_value & 0xFF)
            midi_value = (four_byte_of_int[1] << 16) | (four_byte_of_int[2] << 8) | four_byte_of_int[3]
            self.midi.send(midi_value)
