

from hid_gamepad import Gamepad
import usb_hid


class IntS2WToGamepad:
    """
    A class to convert integer values to corresponding gamepad actions.
    """
    def __init__(self):
        gamepad= Gamepad(usb_hid.devices)
        pass

    def int_to_gamepad(self, int_value: int):
        """
        Convert integer value to gamepad action.
        """
        # Map integer values to gamepad actions
        if int_value == 1:
            self.press_button_a()
        elif int_value == 2:
            self.press_button_b()
        # Add more mappings as needed

    def press_button_a(self):
        # Code to press button A on the gamepad
        pass

    def press_button_b(self):
        # Code to press button B on the gamepad
        pass


    #   gamepad.set_joystick_left_x_percent(random.randrange(-100,100)/100.0)
    #     gamepad.set_joystick_left_y_percent(random.randrange(-100,100)/100.0)
    #     gamepad.set_joystick_right_x_percent(random.randrange(-100,100)/100.0)
    #     gamepad.set_joystick_right_y_percent(random.randrange(-100,100)/100.0)
    #     gamepad.set_trigger_left_percent(random.randrange(0,100)/100.0)
    #     gamepad.set_trigger_right_percent(random.randrange(0,100)/100.0)
    #     button_index= random.randint(1,15)
    #     gamepad.press_buttons(button_index)
    #     time.sleep(1)
    #     gamepad.release_buttons(button_index)
    #     time.sleep(1)
  
    