
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

import time
import board
import digitalio
import usb_hid


   #     time.sleep(3)
    # for _ in range(2):
    #     keyboard.press(Keycode.LEFT_ARROW)
    #     keyboard.release(Keycode.LEFT_ARROW)
    #     time.sleep(1)
    # time.sleep(3)
    # keyboard.press(Keycode.A)
    # keyboard.release(Keycode.A)
    # keyboard.send(Keycode.B)  # Press and release 'A'
    # keyboard.send(Keycode.SHIFT, Keycode.C)  # Press and release 'A' with SHIFT
    # keyboard.send(Keycode.D, Keycode.E)  # Press and release 'A' then 'B'

class IntS2WToKeyboard:

        def __init__(self):
            self.keyboard = Keyboard(usb_hid.devices)
            self.layout = KeyboardLayoutUS(self.keyboard)
            self.cc= ConsumerControl(usb_hid.devices)
            self.int_to_char_map = {
    4032: ' ', 4033: '!', 4034: '"', 4035: '#', 4036: '$', 4037: '%',
    4038: '&', 4039: "'", 4040: '(', 4041: ')', 4042: '*', 4043: '+',
    4044: ',', 4045: '-', 4046: '.', 4047: '/',
    4048: '0', 4049: '1', 4050: '2', 4051: '3', 4052: '4',
    4053: '5', 4054: '6', 4055: '7', 4056: '8', 4057: '9',
    4058: ':', 4059: ';', 4060: '<', 4061: '=', 4062: '>', 4063: '?',
    4064: '@',
    4065: 'A', 4066: 'B', 4067: 'C', 4068: 'D', 4069: 'E',
    4070: 'F', 4071: 'G', 4072: 'H', 4073: 'I', 4074: 'J',
    4075: 'K', 4076: 'L', 4077: 'M', 4078: 'N', 4079: 'O',
    4080: 'P', 4081: 'Q', 4082: 'R', 4083: 'S', 4084: 'T',
    4085: 'U', 4086: 'V', 4087: 'W', 4088: 'X', 4089: 'Y', 4090: 'Z',
    4091: '[', 4092: '\\', 4093: ']', 4094: '^', 4095: '_',
    4096: '`',
    4097: 'a', 4098: 'b', 4099: 'c', 4100: 'd', 4101: 'e',
    4102: 'f', 4103: 'g', 4104: 'h', 4105: 'i', 4106: 'j',
    4107: 'k', 4108: 'l', 4109: 'm', 4110: 'n', 4111: 'o',
    4112: 'p', 4113: 'q', 4114: 'r', 4115: 's', 4116: 't',
    4117: 'u', 4118: 'v', 4119: 'w', 4120: 'x', 4121: 'y', 4122: 'z',
    4123: '{', 4124: '|', 4125: '}', 4126: '~',

    4160: '\u00A0', 4161: '¡', 4162: '¢', 4163: '£', 4164: '¤',
    4165: '¥', 4166: '¦', 4167: '§', 4168: '¨', 4169: '©',
    4170: 'ª', 4171: '«', 4172: '¬', 4174: '®', 4175: '¯',
    4176: '°', 4177: '±', 4178: '²', 4179: '³', 4180: '´',
    4181: 'µ', 4182: '¶', 4183: '·', 4184: '¸', 4185: '¹',
    4186: 'º', 4187: '»', 4188: '¼', 4189: '½', 4190: '¾',
    4191: '¿',

    4192: 'À', 4193: 'Á', 4194: 'Â', 4195: 'Ã', 4196: 'Ä',
    4197: 'Å', 4198: 'Æ', 4199: 'Ç', 4200: 'È', 4201: 'É',
    4202: 'Ê', 4203: 'Ë', 4204: 'Ì', 4205: 'Í', 4206: 'Î',
    4207: 'Ï', 4208: 'Ð', 4209: 'Ñ', 4210: 'Ò', 4211: 'Ó',
    4212: 'Ô', 4213: 'Õ', 4214: 'Ö', 4215: '×', 4216: 'Ø',
    4217: 'Ù', 4218: 'Ú', 4219: 'Û', 4220: 'Ü', 4221: 'Ý',
    4222: 'Þ', 4223: 'ß',

    4224: 'à', 4225: 'á', 4226: 'â', 4227: 'ã', 4228: 'ä',
    4229: 'å', 4230: 'æ', 4231: 'ç', 4232: 'è', 4233: 'é',
    4234: 'ê', 4235: 'ë', 4236: 'ì', 4237: 'í', 4238: 'î',
    4239: 'ï', 4240: 'ð', 4241: 'ñ', 4242: 'ò', 4243: 'ó',
    4244: 'ô', 4245: 'õ', 4246: 'ö', 4247: '÷', 4248: 'ø',
    4249: 'ù', 4250: 'ú', 4251: 'û', 4252: 'ü', 4253: 'ý',
    4254: 'þ', 4255: 'ÿ'
}


        def int_to_keypress(self, value: int):

            if value >= 4000 and value < 5000:
                char_to_type = self.int_to_char_map.get(value, '')
                if char_to_type:
                    self.layout.write(char_to_type)
                # Write text as if typed on a US keyboard
                # self.layout.write("Hello, world!\n")
                return
                

            is_pressing = value >= 1000 and value < 2000
            is_releasing = value >= 2000 and value < 3000

            if is_pressing or is_releasing:
                keycode_value = value % 1000
                keycode_to_apply = None
                print(str(keycode_value))
                if keycode_value < 256:
                    # Backspace 8 0x08 1008 2008
                    try:
                        if keycode_value == 8:
                            keycode_to_apply = Keycode.BACKSPACE
                        # Tab 9 0x09 1009 2009
                        elif keycode_value == 9:
                            keycode_to_apply = Keycode.TAB
                        # Clear 12 0x0C 1012 2012
                        elif keycode_value == 12:
                            keycode_to_apply = Keycode.CLEAR
                        # Enter 13 0x0D 1013 2013
                        elif keycode_value == 13:
                            keycode_to_apply = Keycode.ENTER
                        # Shift 16 0x10 1016 2016
                        elif keycode_value == 16:
                            keycode_to_apply = Keycode.SHIFT
                        # Ctrl 17 0x11 1017 2017
                        elif keycode_value == 17:
                            keycode_to_apply = Keycode.CONTROL
                        # Alt 18 0x12 1018 2018
                        elif keycode_value == 18:
                            keycode_to_apply = Keycode.ALT
                        # Pause 19 0x13 1019 2019
                        elif keycode_value == 19:
                            keycode_to_apply = Keycode.PAUSE
                        # CapsLock 20 0x14 1020 2020
                        elif keycode_value == 20:
                            keycode_to_apply = Keycode.CAPS_LOCK
                        # Escape 27 0x1B 1027 2027
                        elif keycode_value == 27:
                            keycode_to_apply = Keycode.ESCAPE
                        # Space 32 0x20 1032 2032
                        elif keycode_value == 32:
                            keycode_to_apply = Keycode.SPACEBAR
                        # PageUp 33 0x21 1033 2033
                        elif keycode_value == 33:
                            keycode_to_apply = Keycode.PAGE_UP
                        # PageDown 34 0x22 1034 2034
                        elif keycode_value == 34:
                            keycode_to_apply = Keycode.PAGE_DOWN
                        # End 35 0x23 1035 2035
                        elif keycode_value == 35:
                            keycode_to_apply = Keycode.END
                        # Home 36 0x24 1036 2036
                        elif keycode_value == 36:
                            keycode_to_apply = Keycode.HOME
                        # LeftArrow 37 0x25 1037 2037
                        elif keycode_value == 37:
                            keycode_to_apply = Keycode.LEFT_ARROW
                        # UpArrow 38 0x26 1038 2038
                        elif keycode_value == 38:
                            keycode_to_apply = Keycode.UP_ARROW
                        # RightArrow 39 0x27 1039 2039
                        elif keycode_value == 39:
                            keycode_to_apply = Keycode.RIGHT_ARROW
                        # DownArrow 40 0x28 1040 2040
                        elif keycode_value == 40:
                            keycode_to_apply = Keycode.DOWN_ARROW
                        # Select 41 0x29 1041 2041
                        elif keycode_value == 41:
                            keycode_to_apply = Keycode.SELECT
                        # Print 42 0x2A 1042 2042
                        elif keycode_value == 42:
                            keycode_to_apply = Keycode.PRINT_SCREEN
                        # Execute 43 0x2B 1043 2043
                        elif keycode_value == 43:
                            keycode_to_apply = Keycode.EXECUTE
                        # PrintScreen 44 0x2C 1044 2044
                        elif keycode_value == 44:
                            keycode_to_apply = Keycode.PRINT_SCREEN
                        # Insert 45 0x2D 1045 2045
                        elif keycode_value == 45:
                            keycode_to_apply = Keycode.INSERT
                        # Delete 46 0x2E 1046 2046
                        elif keycode_value == 46:
                            keycode_to_apply = Keycode.DELETE
                        # 0 48 0x30 1048 2048
                        elif keycode_value == 48:
                            keycode_to_apply = Keycode.ZERO
                        # 1 49 0x31 1049 2049
                        elif keycode_value == 49:
                            keycode_to_apply = Keycode.ONE
                        # 2 50 0x32 1050 2050
                        elif keycode_value == 50:
                            keycode_to_apply = Keycode.TWO
                        # 3 51 0x33 1051 2051
                        elif keycode_value == 51:
                            keycode_to_apply = Keycode.THREE
                        # 4 52 0x34 1052 2052
                        elif keycode_value == 52:
                            keycode_to_apply = Keycode.FOUR
                        # 5 53 0x35 1053 2053
                        elif keycode_value == 53:
                            keycode_to_apply = Keycode.FIVE
                        # 6 54 0x36 1054 2054
                        elif keycode_value == 54:
                            keycode_to_apply = Keycode.SIX
                        # 7 55 0x37 1055 2055
                        elif keycode_value == 55:
                            keycode_to_apply = Keycode.SEVEN
                        # 8 56 0x38 1056 2056
                        elif keycode_value == 56:
                            keycode_to_apply = Keycode.EIGHT
                        # 9 57 0x39 1057 2057
                        elif keycode_value == 57:
                            keycode_to_apply = Keycode.NINE
                        # A 65 0x41 1065 2065
                        elif keycode_value == 65:
                            keycode_to_apply = Keycode.A
                        # B 66 0x42 1066 2066
                        elif keycode_value == 66:
                            keycode_to_apply = Keycode.B
                        # C 67 0x43 1067 2067
                        elif keycode_value == 67:
                            keycode_to_apply = Keycode.C
                        # D 68 0x44 1068 2068
                        elif keycode_value == 68:
                            keycode_to_apply = Keycode.D
                        # E 69 0x45 1069 2069
                        elif keycode_value == 69:
                            keycode_to_apply = Keycode.E
                        # F 70 0x46 1070 2070
                        elif keycode_value == 70:
                            keycode_to_apply = Keycode.F
                        # G 71 0x47 1071 2071
                        elif keycode_value == 71:
                            keycode_to_apply = Keycode.G
                        # H 72 0x48 1072 2072
                        elif keycode_value == 72:
                            keycode_to_apply = Keycode.H
                        # I 73 0x49 1073 2073
                        elif keycode_value == 73:
                            keycode_to_apply = Keycode.I
                        # J 74 0x4A 1074 2074
                        elif keycode_value == 74:
                            keycode_to_apply = Keycode.J
                        # K 75 0x4B 1075 2075
                        elif keycode_value == 75:
                            keycode_to_apply = Keycode.K
                        # L 76 0x4C 1076 2076
                        elif keycode_value == 76:
                            keycode_to_apply = Keycode.L
                        # M 77 0x4D 1077 2077
                        elif keycode_value == 77:
                            keycode_to_apply = Keycode.M
                        # N 78 0x4E 1078 2078
                        elif keycode_value == 78:
                            keycode_to_apply = Keycode.N
                        # O 79 0x4F 1079 2079
                        elif keycode_value == 79:
                            keycode_to_apply = Keycode.O
                        # P 80 0x50 1080 2080
                        elif keycode_value == 80:
                            keycode_to_apply = Keycode.P
                        # Q 81 0x51 1081 2081
                        elif keycode_value == 81:
                            keycode_to_apply = Keycode.Q
                        # R 82 0x52 1082 2082
                        elif keycode_value == 82:
                            keycode_to_apply = Keycode.R
                        # S 83 0x53 1083 2083
                        elif keycode_value == 83:
                            keycode_to_apply = Keycode.S
                        # T 84 0x54 1084 2084
                        elif keycode_value == 84:
                            keycode_to_apply = Keycode.T
                        # U 85 0x55 1085 2085
                        elif keycode_value == 85:
                            keycode_to_apply = Keycode.U
                        # V 86 0x56 1086 2086
                        elif keycode_value == 86:
                            keycode_to_apply = Keycode.V
                        # W 87 0x57 1087 2087
                        elif keycode_value == 87:
                            keycode_to_apply = Keycode.W
                        # X 88 0x58 1088 2088
                        elif keycode_value == 88:
                            keycode_to_apply = Keycode.X
                        # Y 89 0x59 1089 2089
                        elif keycode_value == 89:
                            keycode_to_apply = Keycode.Y
                        # Z 90 0x5A 1090 2090
                        elif keycode_value == 90:
                            keycode_to_apply = Keycode.Z
                        # LeftWindows 91 0x5B 1091 2091
                        elif keycode_value == 91:
                            keycode_to_apply = Keycode.LEFT_WINDOW_KEY
                        # RightWindows 92 0x5C 1092 2092
                        elif keycode_value == 92:
                            keycode_to_apply = Keycode.RIGHT_WINDOW_KEY
                        # Applications 93 0x5D 1093 2093
                        elif keycode_value == 93:
                            keycode_to_apply = Keycode.APPLICATION
                        # Sleep 95 0x5F 1095 2095
                        elif keycode_value == 95:
                            keycode_to_apply = Keycode.SLEEP
                        # Numpad0 96 0x60 1096 2096
                        elif keycode_value == 96:
                            keycode_to_apply = Keycode.KEYPAD_ZERO
                        # Numpad1 97 0x61 1097 2097
                        elif keycode_value == 97:
                            keycode_to_apply = Keycode.KEYPAD_ONE
                        # Numpad2 98 0x62 1098 2098
                        elif keycode_value == 98:
                            keycode_to_apply = Keycode.KEYPAD_TWO
                        # Numpad3 99 0x63 1099 2099
                        elif keycode_value == 99:
                            keycode_to_apply = Keycode.KEYPAD_THREE
                        # Numpad4 100 0x64 1100 2100
                        elif keycode_value == 100:
                            keycode_to_apply = Keycode.KEYPAD_FOUR
                        # Numpad5 101 0x65 1101 2101
                        elif keycode_value == 101:
                            keycode_to_apply = Keycode.KEYPAD_FIVE
                        # Numpad6 102 0x66 1102 2102
                        elif keycode_value == 102:
                            keycode_to_apply = Keycode.KEYPAD_SIX
                        # Numpad7 103 0x67 1103 2103
                        elif keycode_value == 103:
                            keycode_to_apply = Keycode.KEYPAD_SEVEN
                        # Numpad8 104 0x68 1104 2104
                        elif keycode_value == 104:
                            keycode_to_apply = Keycode.KEYPAD_EIGHT
                        # Numpad9 105 0x69 1105 2105
                        elif keycode_value == 105:
                            keycode_to_apply = Keycode.KEYPAD_NINE
                        # Multiply 106 0x6A 1106 2106
                        elif keycode_value == 106:
                            keycode_to_apply = Keycode.KEYPAD_ASTERISK
                        # Add 107 0x6B 1107 2107
                        elif keycode_value == 107:
                            keycode_to_apply = Keycode.KEYPAD_PLUS
                        # Separator 108 0x6C 1108 2108
                        elif keycode_value == 108:
                            keycode_to_apply = Keycode.KEYPAD_COMMA
                        # Subtract 109 0x6D 1109 2109
                        elif keycode_value == 109:
                            keycode_to_apply = Keycode.KEYPAD_MINUS
                        # Decimal 110 0x6E 1110 2110
                        elif keycode_value == 110:
                            keycode_to_apply = Keycode.KEYPAD_PERIOD
                        # Divide 111 0x6F 1111 2111
                        elif keycode_value == 111:
                            keycode_to_apply = Keycode.KEYPAD_SLASH
                        # F1 112 0x70 1112 2112
                        elif keycode_value == 112:
                            keycode_to_apply = Keycode.F1
                        # F2 113 0x71 1113 2113
                        elif keycode_value == 113:
                            keycode_to_apply = Keycode.F2
                        # F3 114 0x72 1114 2114
                        elif keycode_value == 114:
                            keycode_to_apply = Keycode.F3
                        # F4 115 0x73 1115 2115
                        elif keycode_value == 115:
                            keycode_to_apply = Keycode.F4
                        # F5 116 0x74 1116 2116
                        elif keycode_value == 116:
                            keycode_to_apply = Keycode.F5
                        # F6 117 0x75 1117 2117
                        elif keycode_value == 117:
                            keycode_to_apply = Keycode.F6
                        # F7 118 0x76 1118 2118
                        elif keycode_value == 118:
                            keycode_to_apply = Keycode.F7
                        # F8 119 0x77 1119 2119
                        elif keycode_value == 119:
                            keycode_to_apply = Keycode.F8
                        # F9 120 0x78 1120 2120
                        elif keycode_value == 120:
                            keycode_to_apply = Keycode.F9
                        # F10 121 0x79 1121 2121
                        elif keycode_value == 121:
                            keycode_to_apply = Keycode.F10
                        # F11 122 0x7A 1122 2122
                        elif keycode_value == 122:
                            keycode_to_apply = Keycode.F11
                        # F12 123 0x7B 1123 2123
                        elif keycode_value == 123:
                            keycode_to_apply = Keycode.F12
                        # F13 124 0x7C 1124 2124
                        elif keycode_value == 124:
                            keycode_to_apply = Keycode.F13
                        # F14 125 0x7D 1125 2125
                        elif keycode_value == 125:
                            keycode_to_apply = Keycode.F14
                        # F15 126 0x7E 1126 2126
                        elif keycode_value == 126:
                            keycode_to_apply = Keycode.F15
                        # F16 127 0x7F 1127 2127
                        elif keycode_value == 127:
                            keycode_to_apply = Keycode.F16
                        # F17 128 0x80 1128 2128
                        elif keycode_value == 128:
                            keycode_to_apply = Keycode.F17
                        # F18 129 0x81 1129 2129
                        elif keycode_value == 129:
                            keycode_to_apply = Keycode.F18
                        # F19 130 0x82 1130 2130
                        elif keycode_value == 130:
                            keycode_to_apply = Keycode.F19
                        # F20 131 0x83 1131 2131
                        elif keycode_value == 131:
                            keycode_to_apply = Keycode.F20
                        # F21 132 0x84 1132 2132
                        elif keycode_value == 132:
                            keycode_to_apply = Keycode.F21
                        # F22 133 0x85 1133 2133
                        elif keycode_value == 133:
                            keycode_to_apply = Keycode.F22
                        # F23 134 0x86 1134 2134
                        elif keycode_value == 134:
                            keycode_to_apply = Keycode.F23
                        # F24 135 0x87 1135 2135
                        elif keycode_value == 135:
                            keycode_to_apply = Keycode.F24
                        # NumLock 144 0x90 1144 2144
                        elif keycode_value == 144:
                            keycode_to_apply = Keycode.NUM_LOCK
                        # ScrollLock 145 0x91 1145 2145
                        elif keycode_value == 145:
                            keycode_to_apply = Keycode.SCROLL_LOCK
                        # LeftShift 160 0xA0 1160 2160
                        elif keycode_value == 160:
                            keycode_to_apply = Keycode.LEFT_SHIFT
                        # RightShift 161 0xA1 1161 2161
                        elif keycode_value == 161:
                            keycode_to_apply = Keycode.RIGHT_SHIFT
                        # LeftControl 162 0xA2 1162 2162
                        elif keycode_value == 162:
                            keycode_to_apply = Keycode.LEFT_CONTROL
                        # RightControl 163 0xA3 1163 2163
                        elif keycode_value == 163:
                            keycode_to_apply = Keycode.RIGHT_CONTROL
                        # LeftAlt 164 0xA4 1164 2164
                        elif keycode_value == 164:
                            keycode_to_apply = Keycode.LEFT_ALT
                        # RightAlt 165 0xA5 1165 2165
                        elif keycode_value == 165:
                            keycode_to_apply = Keycode.RIGHT_ALT
                        # BrowserBack 166 0xA6 1166 2166
                        elif keycode_value == 166:
                            keycode_to_apply = Keycode.BROWSER_BACK
                        # BrowserForward 167 0xA7 1167 2167
                        elif keycode_value == 167:
                            keycode_to_apply = Keycode.BROWSER_FORWARD
                        # BrowserRefresh 168 0xA8 1168 2168
                        elif keycode_value == 168:
                            keycode_to_apply = Keycode.BROWSER_REFRESH
                        # BrowserStop 169 0xA9 1169 2169
                        elif keycode_value == 169:
                            keycode_to_apply = Keycode.BROWSER_STOP
                        # BrowserSearch 170 0xAA 1170 2170
                        elif keycode_value == 170:
                            keycode_to_apply = Keycode.BROWSER_SEARCH
                        # BrowserFavorites 171 0xAB 1171 2171
                        elif keycode_value == 171:
                            keycode_to_apply = Keycode.BROWSER_FAVORITES
                        # BrowserHome 172 0xAC 1172 2172
                        elif keycode_value == 172:
                            keycode_to_apply = Keycode.BROWSER_HOME

                        elif keycode_value == 180:
                            keycode_to_apply = Keycode.LAUNCH_MAIL
                        # LaunchMediaSelect 181 0xB5 1181 2181
                        elif keycode_value == 181:
                            keycode_to_apply = Keycode.LAUNCH_MEDIA_PLAYER
                        # LaunchApp1 182 0xB6 1182 2182
                        elif keycode_value == 182:
                            keycode_to_apply = Keycode.LAUNCH_APPLICATION1
                        # LaunchApp2 183 0xB7 1183 2183
                        elif keycode_value == 183:
                            keycode_to_apply = Keycode.LAUNCH_APPLICATION2
                        # OEM1 186 0xBA 1186 2186
                        elif keycode_value == 186:
                            keycode_to_apply = Keycode.OEM_1
                        # OEMPlus 187 0xBB 1187 2187
                        elif keycode_value == 187:
                            keycode_to_apply = Keycode.OEM_PLUS
                        # OEMComma 188 0xBC 1188 2188
                        elif keycode_value == 188:
                            keycode_to_apply = Keycode.OEM_COMMA
                        # OEMMinus 189 0xBD 1189 2189
                        elif keycode_value == 189:
                            keycode_to_apply = Keycode.OEM_MINUS
                        # OEMPeriod 190 0xBE 1190 2190
                        elif keycode_value == 190:
                            keycode_to_apply = Keycode.OEM_PERIOD
                        # OEM2 191 0xBF 1191 2191
                        elif keycode_value == 191:
                            keycode_to_apply = Keycode.OEM_2
                        # OEM3 192 0xC0 1192 2192
                        elif keycode_value == 192:
                            keycode_to_apply = Keycode.OEM_3
                        # OEM4 219 0xDB 1219 2219
                        elif keycode_value == 219:
                            keycode_to_apply = Keycode.OEM_4
                        # OEM5 220 0xDC 1220 2220
                        elif keycode_value == 220:
                            keycode_to_apply = Keycode.OEM_5
                        # OEM6 221 0xDD 1221 2221
                        elif keycode_value == 221:
                            keycode_to_apply = Keycode.OEM_6
                        # OEM7 222 0xDE 1222 2222
                        elif keycode_value == 222:
                            keycode_to_apply = Keycode.OEM_7
                        # OEM8 223 0xDF 1223 2223
                        elif keycode_value == 223:
                            keycode_to_apply = Keycode.OEM_8
                        # OEM102 226 0xE2 1226 2226
                        elif keycode_value == 226:
                            keycode_to_apply = Keycode.OEM_102
                        # ProcessKey 229 0xE5 1229 2229
                        elif keycode_value == 229:
                            keycode_to_apply = Keycode.PROCESS_KEY
                        # Packet 231 0xE7 1231 2231
                        elif keycode_value == 231:
                            keycode_to_apply = Keycode.PACKET
                        # Attn 246 0xF6 1246 2246
                        elif keycode_value == 246:
                            keycode_to_apply = Keycode.ATTN
                        # CrSel 247 0xF7 1247 2247
                        elif keycode_value == 247:
                            keycode_to_apply = Keycode.CRSEL
                        # ExSel 248 0xF8 1248 2248
                        elif keycode_value == 248:
                            keycode_to_apply = Keycode.EXSEL
                        # EraseEOF 249 0xF9 1249 2249
                        elif keycode_value == 249:
                            keycode_to_apply = Keycode.ERASE_EOF

                        # Zoom 251 0xFB 1251 2251
                        elif keycode_value == 251:
                            keycode_to_apply = Keycode.ZOOM
                        # PA1 253 0xFD 1253 2253
                        elif keycode_value == 253:
                            keycode_to_apply = Keycode.PA1
                    except Exception as e:
                        print("Error mapping keycode: " + str(e))
                        

                if keycode_to_apply is not None:
                    
                    print(str(keycode_to_apply))
                    if is_pressing:
                        self.keyboard.press(keycode_to_apply)
                    if is_releasing:
                        self.keyboard.release(keycode_to_apply)
