
import board
import busio



""" Allow to listen from on UART and write to another UART """    
class SingleUartChannelOnPin01:

    def __init__( self):
        ################ UART DEFINITION ################
        # UART0 is used for TTL communication with your computer as Serial Port        
        self.uart0_ttl = busio.UART(board.GP0, board.GP1, baudrate=9600, bits=8, parity=None, stop=1)
        self.char_buffer_array_as_bytes = []
        
    def push_text_to_uart(self, text:str, end_line=True):
        if end_line:
            self.uart0_ttl.write(bytes(text + "\n", "utf-8"))
        else:
            self.uart0_ttl.write(bytes(text, "utf-8"))

    def push_integer_to_uart(self, value: int, end_line=True):
        int_bytes = value.to_bytes(4, "little")
        self.uart0_ttl.write(int_bytes)
        self.uart0_ttl.write(b"0000")
        if end_line:
            self.uart0_ttl.write(b"\n")


    def write(self, data):
        self.uart0_ttl.write(data)
            
    
    def read_and_return_bytes_ended_by_0000(self)->bytes|None:      
        ## I consider that you use only once UART at the same time"""                 
        while self.uart0_ttl.in_waiting > 0:
            self.char_buffer_array_as_bytes.append(self.uart0_ttl.read(1))
        ## if buffer ends with "0000", what ever the side
        buffer_size = len(self.char_buffer_array_as_bytes)
        if buffer_size >= 8 :
            ## use for loop to find a index of 0000 
            ## Tuncate byte in front
            for i in range(buffer_size - 4):
                if self.char_buffer_array_as_bytes[i] == b"0" and \
                   self.char_buffer_array_as_bytes[i+1] == b"0" and \
                   self.char_buffer_array_as_bytes[i+2] == b"0" and \
                   self.char_buffer_array_as_bytes[i+3] == b"0":
                    result = b"".join(self.char_buffer_array_as_bytes[i-4:i+4])
                    self.char_buffer_array_as_bytes = self.char_buffer_array_as_bytes[i+4:]
                    return result
        return None




    



# """ Allow to listen from on UART and write to another UART """    
# class DoubleUartChannel:
#     def __init__( self):
#         ################ UART DEFINITION ################
#         # UART0 is used for TTL communication with your computer as Serial Port
        
#         self.uart0_ttl = busio.UART(board.GP0, board.GP1, baudrate=9600, bits=8, parity=None, stop=1)
#         # UART1 is used for communication with the HC-05 Bluetooth with Android and Quest3
#         self.uart1_hc05 = busio.UART(board.GP4, board.GP5, baudrate=9600, bits=8, parity=None, stop=1)
#         self.char_left = ' '
#         self.char_right = ' '
        
#     def push_text_to_hc05(self, text:str, end_line=True):
#         if end_line:
#             self.uart1_hc05.write(bytes(text + "\n", "utf-8"))
#         else:
#             self.uart1_hc05.write(bytes(text, "utf-8"))

#     def push_text_to_ttl(self, text:str, end_line=True):
#         if end_line:
#             self.uart0_ttl.write(bytes(text + "\n", "utf-8"))
#         else:
#             self.uart0_ttl.write(bytes(text, "utf-8"))

#     def read(self):
#         return self.uart1_hc05.read()

#     def write(self, data):
#         self.uart0_ttl.write(data)
        
#     def get_double_char(self):
#         return self.char_left, self.char_right
    
#     def is_char_right_digit(self):
#         return self.char_right.isdigit()
#     def get_char_left(self):
#         return self.char_left
#     def get_char_right(self):
#         return self.char_right
    
#     def read_and_return_if_right_is_digit(self):      
        
#         ## I consider that you use only once UART at the same time"""                  
#         b= None
#         if self.uart0_ttl.in_waiting > 0:
#             b = self.uart0_ttl.read(1)
#             if b:
#                 self.uart0_ttl.write(b)
                
#         if self.uart1_hc05.in_waiting > 0:
#             b = self.uart1_hc05.read(1)
#             if b:
#                 self.uart1_hc05.write(b)
        
#         if b:
#             print(b)
#             try:
#                 c = b.decode('utf-8')
#                 self.char_left=self.char_right
#                 self.char_right=c
#                 return c.isdigit()
#             except Exception as e:
#                 print("An error occurred:", e)
        
#         return False
        