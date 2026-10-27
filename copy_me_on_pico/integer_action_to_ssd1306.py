
import board
import busio
import displayio
import adafruit_displayio_ssd1306
import random
import i2cdisplaybus
import terminalio
from adafruit_display_text import label


class IntegerActionToSSD1306:
    def __init__(self):
        displayio.release_displays()

        i2c = busio.I2C(board.GP5, board.GP4)

        while not i2c.try_lock():
            pass
        try:
            found_addresses = i2c.scan()
            print("I2C addresses found:", [hex(addr) for addr in found_addresses])
        finally:
            i2c.unlock()

        if 0x3C in found_addresses:
            oled_address = 0x3C
        elif 0x3D in found_addresses:
            oled_address = 0x3D
        elif found_addresses:
            oled_address = found_addresses[0]
        else:
            raise RuntimeError("No I2C display found. Check wiring (SDA/SCL/VCC/GND).")


        display_bus = i2cdisplaybus.I2CDisplayBus(
            i2c,
            device_address=oled_address
        )
        self.display = adafruit_displayio_ssd1306.SSD1306(
            display_bus,
            width=128,
            height=64
        )
        print("OLED ready!")
        self.bitmap = displayio.Bitmap(128, 64, 2)
        self.palette = displayio.Palette(2)
        self.palette[0] = 0x000000
        self.palette[1] = 0xFFFFFF
        self.tile_grid = displayio.TileGrid(self.bitmap, pixel_shader=self.palette)
        self.group = displayio.Group()
        self.group.append(self.tile_grid)
        self.display.root_group = self.group
        self.char_for_a_line_of_8_pixels = 22


    def set_screen_to_text_with_line_return(self, text):
        # Clear the screen first
        self.set_screen_to_black()
        # Split the text into lines
        lines = text.split('\n')
        y = 8
        for line in lines:
            text_area = label.Label(terminalio.FONT, text=line, color=0xFFFFFF)
            text_area.x = 0
            text_area.y = y
            self.group.append(text_area)
            y += 9
        self.display.refresh()

    def set_screen_to_white(self):
        for t in range(0, 128 * 64):
            self.bitmap[t] = 1
        self.display.refresh()

    def set_screen_to_black(self):
        for t in range(0, 128 * 64):
            self.bitmap[t] = 0
        self.display.refresh()

    def set_screen_to_random(self):
        for t in range(0, 128 * 64, 32):
            bits = random.getrandbits(32)
            for b in range(32):
                self.bitmap[t + b] = (bits >> b) & 1
        self.display.refresh()


    def set_screen_to_pixels_with_1024_bytes(self, data):
        for t in range(0, 128 * 64, 8):
            byte_index = t // 8
            bits = data[byte_index]
            for b in range(8):
                self.bitmap[t + b] = (bits >> (7 - b)) & 1
        self.display.refresh()


        


    def set_screen_from_text_image(self, text_image):
        if not text_image:
            self.set_screen_to_black()
            return

        while len(self.group) > 0:
            self.group.pop()

        self.group.append(self.tile_grid)
        self.display.root_group = self.group

        if isinstance(text_image, bytes):
            text_image = text_image.decode("utf-8")
        
        lines = text_image.split('\n')
        pixels = bytearray(128 * 64)
        for y in range(min(64, len(lines))):
            line = lines[y]
            for x in range(min(128, len(line))):
                pixels[y * 128 + x] = 1 if line[x] == "1" else 0

        for t, pixel in enumerate(pixels):
            self.bitmap[t] = pixel
        self.display.refresh()


    def set_screen_from_text_image_of_border(self):
        _image_width = 128
        _image_height = 64
        _image_border_row = "1" * _image_width
        _image_middle_row = "1" + "0" * (_image_width - 2) + "1"
        text_image = "\n".join(
            [_image_border_row]
            + [_image_middle_row] * (_image_height - 2)
            + [_image_border_row]
        ).encode("utf-8")
        self.set_screen_from_text_image(text_image)

