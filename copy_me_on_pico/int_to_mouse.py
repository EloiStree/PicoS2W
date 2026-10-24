from adafruit_hid.mouse import Mouse



import time
import board
import digitalio
import usb_hid

class IntS2WToMouse:
  
    def __init__(self):
        self.mouse = Mouse(usb_hid.devices)


    def int_to_mouse(self, value: int) :
       
        if value == 1260:
           self.mouse.press(Mouse.LEFT_BUTTON)
        elif value == 2260:
           self.mouse.release(Mouse.LEFT_BUTTON)
        elif value == 1261:
           self.mouse.press(Mouse.MIDDLE_BUTTON)
        elif value == 2261:
            self.mouse.release(Mouse.MIDDLE_BUTTON)
        elif value == 1262:
            self.mouse.press(Mouse.RIGHT_BUTTON)
        elif value == 2262:
            self.mouse.release(Mouse.RIGHT_BUTTON)
        elif value == 1263:
            self.mouse.press(Mouse.BUTTON_4)
        elif value == 2263:
            self.mouse.release(Mouse.BUTTON_4)
        elif value == 1264:
            self.mouse.press(Mouse.BUTTON_5)
        elif value == 2264:
            self.mouse.release(Mouse.BUTTON_5)

        elif value  == 1265 or value == 2265:
            self.mouse.click(Mouse.LEFT_BUTTON)
            self.mouse.click(Mouse.LEFT_BUTTON)
        elif value  == 1266 or value == 2266:
            self.mouse.click(Mouse.LEFT_BUTTON)
            self.mouse.click(Mouse.LEFT_BUTTON)
            self.mouse.click(Mouse.LEFT_BUTTON)

        elif value  == 1267 or value == 2267:
            self.mouse.click(Mouse.RIGHT_BUTTON)
            self.mouse.click(Mouse.RIGHT_BUTTON)
        elif value  == 1268 or value == 2268:
            self.mouse.click(Mouse.RIGHT_BUTTON)
            self.mouse.click(Mouse.RIGHT_BUTTON)
            self.mouse.click(Mouse.RIGHT_BUTTON)



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