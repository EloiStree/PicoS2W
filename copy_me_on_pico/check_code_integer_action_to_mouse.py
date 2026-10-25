

import time


from integer_action_to_mouse import IntegerActionToMouse


class CheckCodeIntegerActionToMouse:
    def __init__(self, int_mouse: IntegerActionToMouse):
        self.int_mouse = int_mouse


    def check_move_of_the_mouse(self):                
        int_mouse = self.int_mouse
        m_border_pad = 10
        int_mouse.move_mouse_as_lrdt_of(-4000,-4000)
        for i in range(5):
            int_mouse.move_mouse_as_lrdt_of(50,50)
            time.sleep(0.2)

        for i in range(5):
            int_mouse.scroll_up_of(m_border_pad)
            time.sleep(0.2)

        time.sleep(2)


        for i in range(5):
            int_mouse.scroll_down_of(m_border_pad)
            time.sleep(0.2)

        time.sleep(2)


        int_mouse.move_to_border_top()
        for i in range(5):
            int_mouse.mouse_move_down_of(m_border_pad)
            time.sleep(1)

        int_mouse.move_to_corner_top_right()
        for i in range(5):
            int_mouse.mouse_move_left_down_of(m_border_pad,m_border_pad)
            time.sleep(1)

        int_mouse.move_to_border_right()
        for i in range(5):
            int_mouse.mouse_move_left_of(m_border_pad)
            time.sleep(1)

        int_mouse.move_to_corner_down_right()
        for i in range(5):
            int_mouse.mouse_move_left_up_of(m_border_pad,m_border_pad)
            time.sleep(1)

        int_mouse.move_to_border_down()
        for i in range(5):
            int_mouse.mouse_move_up_of(m_border_pad)
            time.sleep(1)

        int_mouse.move_to_corner_down_left()
        for i in range(5):
            int_mouse.mouse_move_right_up_of(m_border_pad,m_border_pad)
            time.sleep(1)

        int_mouse.move_to_border_left()
        for i in range(5):
            int_mouse.mouse_move_right_of(m_border_pad)
            time.sleep(1)

        int_mouse.move_to_corner_top_left()
        for i in range(5):
            int_mouse.mouse_move_right_down_of(m_border_pad,m_border_pad)
            time.sleep(1)


    def check_click_of_the_mouse(self):
        int_mouse = self.int_mouse
        int_mouse.move_mouse_as_lrdt_of(-4000,-4000)
        press_timing = 1
        for i in range(5):
            int_mouse.move_mouse_as_lrdt_of(50,50)
            time.sleep(0.2)

        for i in range(5):
            int_mouse.click_left_button()
            time.sleep(press_timing)

        for i in range(5):
            int_mouse.click_right_button()
            time.sleep(press_timing)

        for i in range(5):
            int_mouse.click_middle_button()
            time.sleep(press_timing)

        for i in range(5):
            int_mouse.click_button_4()
            time.sleep(press_timing)

        for i in range(5):
            int_mouse.click_button_5()
            time.sleep(press_timing)


        for i in range(5):
            int_mouse.press_left_button()
            time.sleep(press_timing)
            int_mouse.release_left_button()
            time.sleep(press_timing)

        for i in range(5):
            int_mouse.press_right_button()
            time.sleep(press_timing)
            int_mouse.release_right_button()
            time.sleep(press_timing)

        for i in range(5):
            int_mouse.press_middle_button()
            time.sleep(press_timing)
            int_mouse.release_middle_button()
            time.sleep(press_timing)

        for i in range(5):
            int_mouse.press_button_4()
            time.sleep(press_timing)
            int_mouse.release_button_4()
            time.sleep(press_timing)

        for i in range(5):
            int_mouse.press_button_5()
            time.sleep(press_timing)
            int_mouse.release_button_5()
            time.sleep(press_timing) 
