import struct
import board
import busio

# If you want to simulate an Xbox XInput...You cant
# But if you use an Arduino Leonardo you can simulate and XInput Gamepad
# So with a level shifter and Arduino and your Pico you can by Wifi remote controler a XInput
# This code here take the IID format given and and send it to the level shifter for the Arduino
# Arduino dont have NTP and Wifi to sync time but Pico does.
# So you can use the Pico W memory as a queue for the Arduino.



class TransmitterIntToXInputFromLevelShifter:
    """Transmits integer commands to Arduino via UART level shifter for XInput conversion."""

    def __init__(self, uart_tx_pin, uart_rx_pin, baudrate=9600):
        """
        Initialize UART transmitter.
        
        Args:
            uart_tx_pin: TX pin for UART (e.g., board.GP0)
            uart_rx_pin: RX pin for UART (e.g., board.GP1)
            baudrate: Communication speed (default: 9600)
        """
        self.uart_tx_pin = uart_tx_pin
        self.uart_rx_pin = uart_rx_pin
        self.baudrate = baudrate
        # Initialize UART once during construction
        self.uart = busio.UART(uart_tx_pin, uart_rx_pin, baudrate=baudrate)

    def send_integer(self, int_value):
        """
        Send integer command to Arduino.
        
        Args:
            int_value: Integer value to transmit (32-bit signed)
        """
        try:
            byte_array = struct.pack('<i', int_value)
            self.uart.write(byte_array)
        except Exception as e:
            print(f"Error sending integer: {e}")

    def close(self):
        """Close UART connection."""
        if self.uart:
            self.uart.deinit()
