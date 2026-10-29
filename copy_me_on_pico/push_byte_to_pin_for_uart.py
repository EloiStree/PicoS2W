import struct
import board
import busio

# If you want to simulate an Xbox XInput...You cant
# But if you use an Arduino Leonardo you can simulate and XInput Gamepad
# So with a level shifter and Arduino and your Pico you can by Wifi remote controler a XInput
# This code here take the IID format given and and send it to the level shifter for the Arduino
# Arduino dont have NTP and Wifi to sync time but Pico does.
# So you can use the Pico W memory as a queue for the Arduino.


class PushByteToPinForUART:
    """Transmits integer commands to Arduino via UART level shifter for XInput conversion."""

    def __init__(self, p_uart_tx_pin=board.GP0, p_uart_rx_pin=board.GP1, p_baudrate=9600, p_parity=None, p_stop=1):
        """
        Initialize UART transmitter.
        
        Args:
            p_uart_tx_pin: TX pin for UART (e.g., board.GP0)
            p_uart_rx_pin: RX pin for UART (e.g., board.GP1)
            p_baudrate: Communication speed (default: 9600)
            p_parity: UART parity (default: None)
            p_stop: Number of stop bits (default: 1)
        """
        self.uart_tx_pin = p_uart_tx_pin
        self.uart_rx_pin = p_uart_rx_pin
        self.baudrate = p_baudrate
        # Initialize UART once during construction
        self.uart = busio.UART(p_uart_tx_pin, p_uart_rx_pin, baudrate=p_baudrate, parity=p_parity, stop=p_stop)
        self.reset_index = b"\x00\x00\x00\x00"

    def send_integer(self, int_value, with_reset_index=True):
        """
        Send integer command to Arduino.
        
        Args:
            int_value: Integer value to transmit (32-bit signed)
        """
        try:
            byte_array = struct.pack('<i', int_value)
            self.uart.write(byte_array)
            if with_reset_index:
                self.uart.write(self.reset_index) # 
        except Exception as e:
            print(f"Error sending integer: {e}")

    def send_index_with_delay_with_ender_0000(self, index_value, delay_in_milliseconds):
        """
        Send index integer to Arduino with a delay and an ending 0000.
        
        Args:
            index_value: Integer value representing the index (32-bit signed)
            delay_in_milliseconds: Delay in milliseconds after sending the index
        """
        try:
            byte_array = struct.pack('<iii', index_value, delay_in_milliseconds,0)
            self.uart.write(byte_array)
        except Exception as e:
            print(f"Error sending index integer: {e}")

    def send_bytes(self, byte_array):
        """
        Send raw bytes to Arduino.
        
        Args:
            byte_array: Bytes to transmit
        """
        try:
            self.uart.write(byte_array)
        except Exception as e:
            print(f"Error sending bytes: {e}")

    def send_reset_index_0000(self):
        """Send 0000 to reset the index on the Arduino."""
        try:
            self.uart.write(self.reset_index)
        except Exception as e:
            print(f"Error sending index reset: {e}")

    def close(self):
        """Close UART connection."""
        if self.uart:
            self.uart.deinit()
