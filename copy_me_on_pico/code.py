# SOURCE OF THE CODE https://github.com/EloiStree/APIntCodeTournamentHardwarePico2W
# PREVIOUS CODE SOURCE: https://github.com/EloiStree/2024_11_31_ReadHardwareToIndexInteger/tree/main/RaspberryPiPicoW/HelloDefaultInputDUART
# *
# * ----------------------------------------------------------------------------
# * "PIZZA LICENSE":
# * https://github.com/EloiStree wrote this file.
# * As long as you retain this notice you
# * can do whatever you want with this stuff.
# * If you think my code made you win a day of work,
# * send me a good 🍺 or a 🍕 at
# *  - https://www.patreon.com/eloiteaching
# * 
# * You can also support my work by building your own DIY input using Amazon links:
# * - https://github.com/EloiStree/HelloInput
# *
# * May the code be with you.
# *
# * Updated version: https://github.com/EloiStree/License
# * ----------------------------------------------------------------------------
# */


bool_use_debug_print = False

######## PRINT BASIC INFO OF THE DEVICE ########


import sys

from Pico2W.int_delayer import IntTimeDelayer
from int_to_media_player import IntS2WToMediaPlayer
from int_to_midi import IntS2WToMidi
from int_to_keyboard import IntS2WToKeyboard
from int_to_gamepad import IntS2WToGamepad
from int_to_mouse import IntS2WToMouse

print("Hello World")
print(f"sys.implementation: {sys.implementation}")
print(f"sys.version: {sys.version}")
print(f"sys.platform: {sys.platform}")


import time
import board
import busio
import pulseio
import analogio
import random
import struct
import digitalio
import usb_hid
import usb_midi
import adafruit_midi
import time
import ssl
import socketpool
import wifi
import adafruit_requests
import os
import ipaddress
import time
import board
import busio
from digitalio import DigitalInOut
from adafruit_esp32spi import adafruit_esp32spi


# IMPORT FROM NEAR FILE
from hid_gamepad import Gamepad
from wow_int import WowInt
from hc_ttl import HCTTL
from bluetooth_electronics_builder import BluetoothElectronicsBuilder
from int_to_xinput_level_shifter import TransmitterIntToXInputFromLevelShifter

# IMPORT FROM LIB ADAFRUIT

#from keyboard_layout_fr import KeyboardLayoutFR  # Import the French layout
from adafruit_hid.mouse import Mouse
from get_ntp_time import GetNtpUtcTimestampTimeAndDifference


# Do you want to use the Wifi ?
USE_WIFI = True
# Do you want to use the print log ?
USE_PRINT_LOG = True


################# WOW SETTING #################
# Connect to Wi-Fi from setting.toml

# 🐿️ It make the workshop easier to learn
wow = WowInt(True)

# Send a integer message to the server
wow.push(42)

# Send a integer to all champions
# ⚠️ Don't abuse of it in workshop ⚠️rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
wow.lock_push_all()
wow.push_all(42)

# Send a UTF8 message to the server
# 🐿️ It is to check if a connection is working
wow.send_UTF8("Hello World")
     


# 🐿️ If gamepad is not found in usb_hid.devices
# Just reboot the device in boot mode and comeback.
# gamepad= Gamepad(usb_hid.devices)           # Start behaving as gamepad
# mouse  = Mouse(usb_hid.devices)             # Start behaving as mouse
# consumer = ConsumerControl(usb_hid.devices) # Start behaving as media control
# keyboard = Keyboard(usb_hid.devices)
# midi = adafruit_midi.MIDI(midi_in=usb_midi.ports[0], midi_out=usb_midi.ports[1], in_channel=0, out_channel=0)
# hcttl= HCTTL() # Start behaving as  HC05 (4 5) listener and TTL(0 1) sender
be = BluetoothElectronicsBuilder()
int_xbox = TransmitterIntToXInputFromLevelShifter(board.GP0, board.GP1) # TX0 RX1 to level shifter to Arduino Leonardo
int_midi = IntS2WToMidi() # Start behaving as Integer to MIDI converter
int_media_player = IntS2WToMediaPlayer()
int_keyboard = IntS2WToKeyboard()
int_gamepad = IntS2WToGamepad()
int_mouse = IntS2WToMouse()
int_delayer = IntTimeDelayer()
ntp_time_difference = GetNtpUtcTimestampTimeAndDifference()
print("RTC ms:", ntp_time_difference.get_local_timestamp_in_milliseconds())
print("NTP ms:", ntp_time_difference.get_ntp_utc_timestamp_in_milliseconds())
print("Drift (ms):", ntp_time_difference.get_local_to_ntp_utc_difference_milliseconds())

def relay_or_interpret_value(int_index:int,int_value:int, ulong_date_timestamp_ntp:int):
        # If tag is 17 or 18 then it is a gamepad xinput controller and need to be level shifted to a Arduino Leonardo
        # If tag is between 1300 and 1398 then it is a on off gamepad xinput controller
        # if it is not a xinput then deal with it.
        int_tag = int(int_value / 100000000 % 100)
        if bool_use_debug_print:
            print(f"Tag:{int_tag} Index:{int_index} Value:{int_value} Timestamp:{ulong_date_timestamp_ntp}")

        if (int_value > 1300 and int_value < 1399) or (int_value > 2300 and int_value < 2399) or int_tag==18 or int_tag==17:
            # It is a xinput gamepad commandxbox.send_integer(int_value)
            if ulong_date_timestamp_ntp==0:
               
                if bool_use_debug_print:
                    print (f"Send XInput Integer without timestamp: {int_value}")
                if bool_use_debug_print:
                    print (f"As bytes : {struct.pack('<i', int_value)}")
                int_xbox.send_integer(int_value)
        else:    
            int_midi.int_to_midi(int_value)
            int_media_player.int_to_control(int_value)
            int_keyboard.int_to_keypress(int_value)
            int_gamepad.int_to_gamepad(int_value)
            int_mouse.int_to_mouse(int_value)



if True: # Listen to incoming udp package on port 3615
    
    # Create socket pool
    pool = socketpool.SocketPool(wifi.radio)

    # Create UDP socket
    sock = pool.socket(pool.AF_INET, pool.SOCK_DGRAM)

    # Bind to all interfaces on port 5005
    UDP_PORT = 3615
    sock.bind(("0.0.0.0", UDP_PORT))
    sock.settimeout(None)  # blocking mode

    print(f"Listening for UDP packets on port {UDP_PORT}...")
    buffer = bytearray(1024)

    while True:
        size, addr = sock.recvfrom_into(buffer)
        data = buffer[:size]
        if bool_use_debug_print:
            print("Received from", addr, ":", data)

        lenght_package = len(data)
        if lenght_package not in [4,8,12,16]:
                if lenght_package % 16 == 0:
                    # This is a macro package with several IID
                    #splite the array in several package of 16 bytes
                    number_of_package = int(lenght_package / 16)
                    if bool_use_debug_print:
                        print("Macro package with number of package:", number_of_package)
                    for i in range(number_of_package):
                        data_part = data[i*16:(i+1)*16]
                        int_index, int_value, ulong_date = struct.unpack('<iiQ', data_part)

                        print(f"Index: {int_index}, Value: {int_value}, Timestamp: {ulong_date}")
                        # I AM HERE
                        # I NEED TO ADD A Index Value Date class to store in relay
                        # if the time is under 1000 *60 *30 (30 minutes) = 1 800 000 ms
                        # then it is a relative time from now and can be stack in the coming iid.
                        # I need to create a delayer for iid with macro relative time
                        # relay_or_interpret_value(int_index,int_value,ulong_date)
                        


                else:
                    print("Invalid package length:", lenght_package)
        else:
            int_value = 0
            int_index = 0
            if lenght_package == 4:
                int_value = struct.unpack('<i', data)[0]
                if bool_use_debug_print:
                    print("Unpacked Integer:", int_value)
                relay_or_interpret_value(0,int_value,0)
            elif lenght_package == 8:
                int_index, int_value = struct.unpack('<ii', data)
                if bool_use_debug_print:
                    print("Unpacked Two Integers:", int_index, int_value)
                relay_or_interpret_value(int_index,int_value,0)
            elif lenght_package == 12:
                int_value, uint64 = struct.unpack('<iQ', data)
                if bool_use_debug_print:
                    print("Unpacked Integer and Unsigned Long:", int_value, uint64)
                relay_or_interpret_value(0,int_value,uint64)
            elif lenght_package == 16:
                int_index, int_value, uint64 = struct.unpack('<iiQ', data)
                print("Unpacked Two Integers and One Unsigned Long:", int_index, int_value, uint64)
                relay_or_interpret_value(int_index,int_value,uint64)





# if False: # EXPERIMENT WITH BLUETOOTH ELECTRONICS 🏳️
#     while True:
#         #LABEL
#         date = str(time.monotonic())
#         text = be.create_text('p',"Hello"+date)
#         hcttl.push_text_to_hc05(text)
#         text = be.create_light_random_color('L')
#         # SOUND
#         hcttl.push_text_to_hc05(text)
#         text =be.create_sound('S',random.randint(0,100))
#         hcttl.push_text_to_hc05(text)
#         text =be.create_gauge('D',random.randint(0,100))
#         hcttl.push_text_to_hc05(text)
#         # GAUGE 
#         text = be.create_gauge_orange(value=random.randint(0,100))
#         hcttl.push_text_to_hc05(text)
#         text = be.create_temperature(value=random.randint(0,100))
#         hcttl.push_text_to_hc05(text)
#         text = be.create_gauge_blue(value=random.randint(0,100))
#         hcttl.push_text_to_hc05(text)
        
#         # GRAPH        
#         time.sleep(1)
#         text = be.create_graph_clear('H')
#         hcttl.push_text_to_hc05(text)
#         for i in range(10):
#             text = be.create_graph_add('H',i,random.randint(0,100),i+1,random.randint(0,100))
#             time.sleep(0.1)
#             hcttl.push_text_to_hc05(text)
#         time.sleep(1)


# # Example of how to use midi in adafruit_midi.py
# if False: # EXPERIMENT WITH MIDI 🏳️
#     while True:
#         value127= random.randint(30,100)
#         velocity127= random.randint(40,127)
#         midi.send(NoteOn(value127, velocity127))
#         time.sleep(1)
#         midi.send(NoteOff(value127, 0))
#         time.sleep(1)
 
# # Example of how to use the keyboard in adafruit_hid.keyboard.py
# if False: # EXPERIMENT WITH KEYBOARD 🏳️
#     time.sleep(3)
#     for _ in range(2):
#         keyboard.press(Keycode.LEFT_ARROW)
#         keyboard.release(Keycode.LEFT_ARROW)
#         time.sleep(1)
#     time.sleep(3)
#     keyboard.press(Keycode.A)
#     keyboard.release(Keycode.A)
#     keyboard.send(Keycode.B)  # Press and release 'A'
#     keyboard.send(Keycode.SHIFT, Keycode.C)  # Press and release 'A' with SHIFT
#     keyboard.send(Keycode.D, Keycode.E)  # Press and release 'A' then 'B'

# Example of how to use the gamepad in hid_gamepad.py
# if False: # EXPERIMENT WITH GAMEPAD 🏳️
#     while True:
#         gamepad.set_joystick_left_x_percent(random.randrange(-100,100)/100.0)
#         gamepad.set_joystick_left_y_percent(random.randrange(-100,100)/100.0)
#         gamepad.set_joystick_right_x_percent(random.randrange(-100,100)/100.0)
#         gamepad.set_joystick_right_y_percent(random.randrange(-100,100)/100.0)
#         gamepad.set_trigger_left_percent(random.randrange(0,100)/100.0)
#         gamepad.set_trigger_right_percent(random.randrange(0,100)/100.0)
#         button_index= random.randint(1,15)
#         gamepad.press_buttons(button_index)
#         time.sleep(1)
#         gamepad.release_buttons(button_index)
#         time.sleep(1)

# Example of how to use the mouse in adafruit_hid.mouse.py
# if False: # EXPERIMENT WITH MOUSE 🏳️
#     for _ in range(10):
#         mouse.move(x=10, y=10, wheel=0)
#         mouse.press(Mouse.LEFT_BUTTON)
#         mouse.release(Mouse.LEFT_BUTTON)
    
# Example of how to use the consumer in adafruit_hid.consumer_control.py
# if False: # EXPERIMENT WITH MEDIA 🏳️
#     consumer.send(ConsumerControlCode.PLAY_PAUSE)  # Play/Pause media
#     for _ in range(100):
#         consumer.send(ConsumerControlCode.VOLUME_INCREMENT)
#     consumer.send(ConsumerControlCode.VOLUME_INCREMENT)  # Increase volume
#     consumer.send(ConsumerControlCode.VOLUME_DECREMENT)  # Decrease volume

############## PINS REMINDER ##############
## DIGITAL PIN ARE 0 OR 1
## Those are the pin that you can use for IO (Input/Output) communication
# pins_id_digital = [
#     board.GP2, board.GP3,  board.GP6,
#     board.GP7, board.GP8, board.GP9, board.GP10, board.GP11,
#     board.GP12, board.GP13, board.GP14, board.GP15, board.GP16,
#     board.GP17, board.GP18, board.GP19, board.GP20, board.GP21,
#     board.GP22
# ]
# ## ANALOG PIN ARE 0 TO 65535
# ## Those are the pin that you can use for analog communication 
# pins_id_analog = [
#    board.GP26, board.GP27, board.GP28
# ]
# ## UART PIN ARE RESERVED TO MAKE SERIAL COMMUNICATION
# pins_id_UART=[
#     board.GP0, board.GP1, # UART0
#     board.GP4, board.GP5  # UART1
# ]





# ################# PIN DEFINITION #################
# # To ease the learning curved, I prepared a joystick and trigger (potentiometer) with a button
# pin_A27_XJoystick = analogio.AnalogIn(board.GP27)
# pin_A26_YJoystick = analogio.AnalogIn(board.GP26)
# pin_A28_ZJoystick = analogio.AnalogIn(board.GP28)
# pin_D22_Button = digitalio.DigitalInOut(board.GP22)
# pin_D22_Button.direction = digitalio.Direction.INPUT
# pin_D22_Button.pull = digitalio.Pull.UP
# pin_D21_3v3 = digitalio.DigitalInOut(board.GP21)
# pin_D21_3v3.direction = digitalio.Direction.OUTPUT
# pin_D21_3v3.value = True


# if False:
#     ## Read a pin in PULL UP
#     ## Some button are better with a pull up, some with a pull down
#     pin_GP17 = digitalio.DigitalInOut(board.GP17)
#     pin_GP17.direction = digitalio.Direction.INPUT
#     pin_GP17.pull = digitalio.Pull.UP
#     bool_value = not pin_GP17.value
#     print(f"Pin 17 PULL UP: {pin_GP17.value}")
    
#     ## Read a pin in PULL DOWN
#     pin_GP16 = digitalio.DigitalInOut(board.GP16)
#     pin_GP16.direction = digitalio.Direction.INPUT
#     pin_GP16.pull = digitalio.Pull.DOWN
#     bool_value = pin_GP17.value
#     print(f"Pin 16 PULL DOWN: {pin_GP17.value}")
    
#     ## Write a pin as OUTPUT
#     pin_GP15 = digitalio.DigitalInOut(board.GP15)
#     pin_GP15.direction = digitalio.Direction.OUPUT
#     pin_GP15.value = True
#     print(f"Pin 15 OUTPUT: {pin_GP15.value}")
    



# def uartToAction(c0, c1):
#     """C0 is the first left character and C1 is the second right character"""
#     timestamp_ms = int(time.monotonic() * 1000)
#     if USE_PRINT_LOG:
#         print("Timestamp in milliseconds:", timestamp_ms)
#         print(f"C0:{c0} C1:{c1}")
#     if c1 == '1':
#         if c0 == 'A':
#             print("Add Code")
#         elif c0 == 'B':
#             print("Add Code")
#         elif c0 == 'C':
#             print("Add Code")
#         elif c0 == 'D':
#             print("Add Code")
#     elif c1== '2':
#         if c0=='L':
#             wow.push(1037)
#         elif c0=='l':
#             wow.push(2037)
            
#         elif c0=='D':
#             wow.push(1040)
#         elif c0=='d':
#             wow.push(2040)
#         elif c0=='R':
#             wow.push(1039)
#         elif c0=='r':
#             wow.push(2039)
#         elif c0=='U':
#             wow.push(1038)
#         elif c0=='u':
#             wow.push(2038)
#         elif c0=='T':
#             wow.push(1009)
#         elif c0=='t':
#             wow.push(2009)
#         elif c0=='E':
#             wow.push(1013)
#         elif c0=='e':
#             wow.push(2013)
#         elif c0=='S':
#             wow.push(1032)
#         elif c0=='s':
#             wow.push(2032)
#         elif c0=='I':
#             wow.push(1087)
#         elif c0=='i':
#             wow.push(2087)
#         elif c0=='O':
#             wow.push(1088)
#         elif c0=='o':
#             wow.push(2088)
    
   


# ## Example of how to use the joystick and trigger in loop
# use_learning_loop = False
# if use_learning_loop:
    
#     # Store the current and previous value to detect change
#     # Joystick
#     bool_is_joystick_left = False
#     bool_is_joystick_right = False
#     bool_is_joystick_up = False
#     bool_is_joystick_down = False
#     bool_is_joystick_left_previous = False
#     bool_is_joystick_right_previous = False
#     bool_is_joystick_up_previous = False
#     bool_is_joystick_down_previous = False
#     # Trigger
#     bool_is_trigger_down = False
#     bool_is_trigger_up = False
#     bool_is_trigger_down_previous = False
#     bool_is_trigger_up_previous = False
#     # Button
#     bool_is_button_down_previous = False
#     bool_is_button_down= False
    
#     # Joystick death zoner to detect left, right up, down are active
#     int_joystick_death_zone = 0.8
#     while True:
        
#         # CHECK IF A UART HAVE SOME COMMAND FOR USE STORE ON TWO CHARS FROM HC05 OR TTL
#         if hcttl.read_and_return_if_right_is_digit():
#             # If the right char is a digit, it means that we received a command
#             charOne, charTwo = hcttl.get_double_char()
#             uartToAction(charOne, charTwo)
        
#         # read and convert the value from the analog pin.
#         bool_print_joystick=False
#         joystick_x = pin_A27_XJoystick.value
#         joystick_y = pin_A26_YJoystick.value
#         joystick_x_127 = max(-127, min(127, int((joystick_x / 65535) * 254 - 127)))
#         joystick_y_127 = max(-127, min(127, int((joystick_y / 65535) * 254 - 127)))
#         joystick_y_percent = joystick_y_127 / 127.0
#         joystick_x_percent = joystick_x_127 / 127.0
#         trigger = pin_A28_ZJoystick.value
#         trigger_min=0
#         trigger_max=65535
#         trigger_255 = max(0, min(255, int((trigger - trigger_min) / (trigger_max - trigger_min) * 255)))
#         trigger_percent = trigger_255 / 255.0
        
        
#         # Set the value of the joystick and trigger for debugging purpose
#         gamepad.set_joystick_left_x_127(joystick_x_127)
#         gamepad.set_joystick_left_y_127(joystick_y_127)
#         gamepad.set_trigger_left_255(trigger_255)
     
        
#         # Check from the analog value if the zone are reached
#         bool_is_button_down = not pin_D22_Button.value
#         if joystick_x_percent < -int_joystick_death_zone:
#             bool_is_joystick_left = True
#             bool_is_joystick_right = False
#         elif joystick_x_percent > int_joystick_death_zone:
#             bool_is_joystick_left = False
#             bool_is_joystick_right = True
#         else:
#             bool_is_joystick_left = False
#             bool_is_joystick_right = False
        
#         if joystick_y_percent < -int_joystick_death_zone:
#             bool_is_joystick_up = True
#             bool_is_joystick_down = False
#         elif joystick_y_percent > int_joystick_death_zone:
#             bool_is_joystick_up = False
#             bool_is_joystick_down = True
#         else:
#             bool_is_joystick_up = False
#             bool_is_joystick_down = False
            
            
#         if trigger_percent > 0.8:
#             bool_is_trigger_up = True
#         else:
#             bool_is_trigger_up = False
            
            
#         if trigger_percent <0.2:
#             bool_is_trigger_down = True
#         else:
#             bool_is_trigger_down = False
        
#         # Check for any changed of zone
#         if bool_is_button_down != bool_is_button_down_previous:
#             bool_is_button_down_previous = bool_is_button_down
#             if bool_is_button_down:
#                 print("Button Down Start")
#                 wow.push(1032)
#             else:
#                 print("Button Down End")
#                 wow.push(2032)
#             bool_print_joystick=True
        
#         if bool_is_joystick_left != bool_is_joystick_left_previous:
#             bool_is_joystick_left_previous = bool_is_joystick_left
#             if bool_is_joystick_left:
#                 print("Joystick Left Start")
#                 wow.push(1037)
#             else:
#                 print("Joystick Left End")
#                 wow.push(2037)
#             bool_print_joystick=True
                
#         if bool_is_joystick_right != bool_is_joystick_right_previous:
#             bool_is_joystick_right_previous = bool_is_joystick_right
#             if bool_is_joystick_right:
#                 print("Joystick Right Start")
#                 wow.push(1039)
#             else:
#                 print("Joystick Right End")
#                 wow.push(2039)
#             bool_print_joystick=True
                
#         if bool_is_joystick_up != bool_is_joystick_up_previous:
#             bool_is_joystick_up_previous = bool_is_joystick_up
#             if bool_is_joystick_up:
#                 print("Joystick Up Start")
#                 wow.push(1038)
#             else:
#                 print("Joystick Up End")
#                 wow.push(2038)
#             bool_print_joystick=True
            
#         if bool_is_joystick_down != bool_is_joystick_down_previous:
#             bool_is_joystick_down_previous = bool_is_joystick_down
#             if bool_is_joystick_down:
#                 print("Joystick Down Start")
#                 wow.push(1040)
#             else:
#                 print("Joystick Down End")
#                 wow.push(2040)
#             bool_print_joystick=True
        
        
#         if bool_is_trigger_down != bool_is_trigger_down_previous:
#             bool_is_trigger_down_previous = bool_is_trigger_down
#             if bool_is_trigger_down:
#                 print("Trigger Down Start")
#                 wow.push(1009)
#             else:
#                 print("Trigger Down End")
#                 wow.push(2009)
#             bool_print_joystick=True
            
#         if bool_is_trigger_up != bool_is_trigger_up_previous:
#             bool_is_trigger_up_previous = bool_is_trigger_up
#             if bool_is_trigger_up:
#                 print("Trigger Up Start")
#                 wow.push(1032)
#             else:
#                 print("Trigger Up End")
#                 wow.push(2032)
#             bool_print_joystick=True
        
        
#         if bool_print_joystick:
#             print(f"Joystick x{joystick_x_127} y{joystick_y_127} / x{joystick_x} y{joystick_y}")
#             print(f"Trigger {trigger_255}  / {trigger}")
       
        
#         # Avoid excessive looping
#         time.sleep(0.00001)
        







