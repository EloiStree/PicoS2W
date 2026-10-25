"""
The aim of this script is to simulate mouse actions with what the Pico W provides.
DOC: https://github.com/EloiStree/S2W/blob/main/README.md
"""


## TEST ON GAME:
"""
- https://orteil.dashnet.org/cookieclicker/
- https://redragonshop.com/pages/mouse-tester
"""


## DOC: https://docs.circuitpython.org/projects/hid/en/latest/api.html#adafruit-hid-mouse-mouse
import os

from adafruit_hid.mouse import Mouse
import time
import usb_hid
from absolute_mouse import Mouse


""" CHEAT SHEET
mouse.move(x=20)          # Move right
mouse.move(x=-20)         # Move left
mouse.move(y=20)          # Move down
mouse.move(y=-20)         # Move up
mouse.move(x=10, y=5)     # Diagonal movement
mouse.move(wheel=1)       # Scroll up
mouse.move(wheel=-1)      # Scroll down
mouse.click(Mouse.RIGHT_BUTTON)
mouse.press(Mouse.LEFT_BUTTON)
mouse.release(Mouse.LEFT_BUTTON)    
mouse.release_all()
mouse.move(pan=1)    # Scroll right
mouse.move(pan=-1)   # Scroll left
"""

import time
import board
import digitalio
import usb_hid

class IntegerActionToMouse:
  
    def __init__(self):
        self.mouse = Mouse(usb_hid.devices)
        self.target_width_resolution = int(os.getenv("TARGET_SCREEN_RESOLUTION_WIDTH", 1920))
        self.target_height_resolution = int(os.getenv("TARGET_SCREEN_RESOLUTION_HEIGHT", 1080))


    def int_to_mouse(self, value: int) :
       
        if value == 1260:
           self.press_left_button()
        elif value == 2260:
            self.release_left_button()
        elif value == 1261:
            self.press_middle_button()
        elif value == 2261:
            self.release_middle_button()
        elif value == 1262:
            self.press_right_button()
        elif value == 2262:
            self.release_right_button()
        elif value == 1263:
            self.press_button_4()
        elif value == 2263:
            self.release_button_4()
        elif value == 1264:
            self.press_button_5()
        elif value == 2264:
            self.release_button_5()

        elif value  == 1265:
            ## Double Click Left
            self.click_left_button()
            self.click_left_button()
        elif value  == 1266:
            ## Triple Click Left
            self.click_left_button()
            self.click_left_button()
            self.click_left_button()

        elif value  == 1267:
            ## Double Click Right
            self.click_right_button()
            self.click_right_button()
        elif value  == 1268:
            ## Triple Click Right
            self.click_right_button()
            self.click_right_button()
            self.click_right_button()

        elif value == 1268 :
            self.scroll_up()
        elif value == 1269 :
            self.scroll_down()
        elif value == 1270 :
            self.scroll_left()
        elif value == 1271 :
            self.scroll_right()
        elif value == 1272 :
            self.move_to_border_top()
        elif value == 1273 :
            self.move_to_corner_top_right()
        elif value == 1274 :
            self.move_to_border_right()
        elif value == 1275 :
            self.move_to_corner_down_right()
        elif value == 1276 :
            self.move_to_border_down()
        elif value == 1277 :
            self.move_to_corner_down_left()
        elif value == 1278 :
            self.move_to_border_left()
        elif value == 1279 :
            self.move_to_corner_top_left()
        else:
            ## What happening https://github.com/EloiStree/S2W look at Mouse
            if value >= 1400000000 and value < 1600000000:
                # ~pico|1425002500> in GOMI
                # ~pico|1450005000> in GOMI
                value_without_prefix = value % 100000000
                x_left_right_percent = (value_without_prefix / 10000.0) / 10000.0
                y_down_top_percent = (value_without_prefix % 10000.0) / 10000.0
                x_left_right_32767 = int(x_left_right_percent * 32767.0)
                y_down_top_32767 = int(y_down_top_percent * 32767.0)
                print(f"x_left_right_percent: {x_left_right_percent}, y_down_top_percent: {y_down_top_percent}")

                #Using mouse absolute as replacement of adafruit mouse
                #self.mouse.move(x_left_right_32767, y_down_top_32767)

                self.move_mouse_at_lrdt_percent_of(x_left_right_percent, y_down_top_percent)


            elif value >= 1600000000 and value < 1700000000:
                # Workd with adafruit. but the absolute mouse override it.
                # I need to understand it better or make a cross on it.
                # The adafruit is not good enought any way as it is not per pixel move.
                pass
                # # ~pico|1651005010> in GOMI
                # # ~pico|1600500050> in GOMI
                # value_without_prefix = value % 100000000
                # x_left_right_pixel = (value_without_prefix) / 10000.0
                # y_down_top_pixel = value_without_prefix % 10000
                # print(f"value_without_prefix: {value_without_prefix}")
                # print(f"x_left_right_pixel: {x_left_right_pixel}, y_down_top_pixel: {y_down_top_pixel}")
                # if x_left_right_pixel>5000:
                #     x_left_right_pixel=-(x_left_right_pixel-5000)

                # if y_down_top_pixel>5000:
                #     y_down_top_pixel=-(y_down_top_pixel-5000)

                # print(f"DDD x_left_right_pixel: {x_left_right_pixel}, y_down_top_pixel: {y_down_top_pixel}")
                # self.move_mouse_as_lrdt_of(int(x_left_right_pixel), int(y_down_top_pixel))




        # # Move Up 2001
        # if value == 2001:
        #      self.mouse.move(y=-10)
        # # Move Down 2002
        # elif value == 2002:
        #      self.mouse.move(y=10)
        # # Move Left 2003
        # elif value == 2003:
        #      self.mouse.move(x=-10)
        # # Move Right 2004
        # elif value == 2004:
        #      self.mouse.move(x=10)
        # # Left Click 2010
        # elif value == 2010:
        #      self.mouse.click(Mouse.LEFT_BUTTON)
        # # Right Click 2011
        # elif value == 2011:
        #      self.mouse.click(Mouse.RIGHT_BUTTON)
        # else:
        #     pass

    #     if False: # EXPERIMENT WITH MOUSE 🏳️
    # for _ in range(10):
    #     mouse.move(x=10, y=10, wheel=0)
    #     mouse.press(Mouse.LEFT_BUTTON)
    #     mouse.release(Mouse.LEFT_BUTTON)


#region MOUSE CLICKING

    def press_left_button(self):
        self.mouse.press(Mouse.LEFT_BUTTON)

    def release_left_button(self):
        self.mouse.release(Mouse.LEFT_BUTTON)

    def press_middle_button(self):
        self.mouse.press(Mouse.MIDDLE_BUTTON)

    def release_middle_button(self):
        self.mouse.release(Mouse.MIDDLE_BUTTON)

    def press_right_button(self):
        self.mouse.press(Mouse.RIGHT_BUTTON)

    def release_right_button(self):
        self.mouse.release(Mouse.RIGHT_BUTTON)

    def press_button_4(self):
        self.mouse.press(Mouse.BUTTON_4)

    def release_button_4(self):
        self.mouse.release(Mouse.BUTTON_4)

    def press_button_5(self):
        self.mouse.press(Mouse.BUTTON_5)

    def release_button_5(self):
        self.mouse.release(Mouse.BUTTON_5)


    def click_left_button(self):
        self.mouse.click(Mouse.LEFT_BUTTON)

    def click_right_button(self):
        self.mouse.click(Mouse.RIGHT_BUTTON)

    def click_middle_button(self):
        self.mouse.click(Mouse.MIDDLE_BUTTON)

    def click_button_4(self):
        self.mouse.click(Mouse.BUTTON_4)

    def click_button_5(self):
        self.mouse.click(Mouse.BUTTON_5)

#endregion MOUSE CLICKING


    ## UP IS AWAY FROM THE USER
    def scroll_up_of(self, amount=10):
        self.mouse.move(wheel=amount)
  
    ## DOWN IS TOWARDS THE USER  
    def scroll_down_of(self, amount=10):
        self.mouse.move(wheel=-amount)

    def scroll_left_of(self, amount=10):
        self.mouse.move(pan=-amount)

    def scroll_right_of(self, amount=10):
        self.mouse.move(pan=amount)


    def release_all_mouse_buttons(self):
        self.mouse.release_all()


    def move_mouse_at_lrdt_percent_of(self, left_to_right=0.0, down_top=0.0):
        self.mouse.move(int(32767.0*left_to_right), int(32767.0*(1.0-down_top)))


    def move_to_border_left(self):
        self.move_mouse_at_lrdt_percent_of(left_to_right=0, down_top=0.5)

    def move_to_border_right(self):
        self.move_mouse_at_lrdt_percent_of(left_to_right=1, down_top=0.5)

    def move_to_border_top(self):
        self.move_mouse_at_lrdt_percent_of(left_to_right=0.5, down_top=0)

    def move_to_border_down(self):
        self.move_mouse_at_lrdt_percent_of(left_to_right=0.5, down_top=1)

    def move_to_corner_top_left(self):
        self.move_mouse_at_lrdt_percent_of(left_to_right=0, down_top=0)

    def move_to_corner_top_right(self):
        self.move_mouse_at_lrdt_percent_of(left_to_right=1, down_top=0)

    def move_to_corner_down_left(self):
        self.move_mouse_at_lrdt_percent_of(left_to_right=0, down_top=1)

    def move_to_corner_down_right(self):
        self.move_mouse_at_lrdt_percent_of(left_to_right=1, down_top=1)

    





    # def mouse_move_left_up_of(self, left=0, up=0):
    #     self.move_mouse_as_lrdt_of(left_to_right=-left, down_top=up)

    # def mouse_move_right_up_of(self, right=0, up=0):
    #     self.move_mouse_as_lrdt_of(left_to_right=right, down_top=up)

    # def mouse_move_left_down_of(self, left=0, down=0):
    #     self.move_mouse_as_lrdt_of(left_to_right=-left, down_top=-down)

    # def mouse_move_right_down_of(self, right=0, down=0):
    #     self.move_mouse_as_lrdt_of(left_to_right=right, down_top=-down)

    # def mouse_move_up_of(self, up=0):
    #     self.move_mouse_as_lrdt_of(down_top=up)

    # def mouse_move_down_of(self, down=0):
    #     self.move_mouse_as_lrdt_of(down_top=-down)   

    # def mouse_move_left_of(self, left=0):
    #     self.move_mouse_as_lrdt_of(left_to_right=-left)

    # def mouse_move_right_of(self, right=0):
    #     self.move_mouse_as_lrdt_of(left_to_right=right)


    # def _move_mouse_as_piece_of(self, left_to_right=0, down_top=0):
    #     # HID limitation is 127  so move by 100 distance pack
    #     # NOTE FOR ME MOUSE ARE SUBJECT TO ACCELERATION
    #     # MAY BE TRY TO CORRECT WITH THIS CODE
    #     # https://circuitpython-absolute-mouse.readthedocs.io/en/latest/
    #     while left_to_right != 0 or down_top != 0:
    #         move_x = max(min(left_to_right, 100), -100)
    #         move_y = max(min(down_top, 100), -100)
    #         self.mouse.move(x=move_x, y=-move_y)
    #         left_to_right -= move_x
    #         down_top -= move_y
