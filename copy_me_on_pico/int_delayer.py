import time

## This class holds an integer and the time at which it should be executed
class IntToDelayValue:
    def __init__(self, integer, when_to_execute):
        self.m_integer = integer
        self.m_when_to_execute = when_to_execute


## The aim of this code is to delay integer to it execution time requested by the user in milliseconds
class IntTimeDelayer:

    def __init__(self, rtc_time_seconds=0.0, timezone_offset_seconds=0.0):
        self.delays_integer = []
        self._mono_ref = time.monotonic()
        self._rtc_ref = rtc_time_seconds
        self.tz_offset = timezone_offset_seconds

    def get_current_time_on_pico_2w(self):
        return self.get_local_timestamp_in_milliseconds()

    def get_local_timestamp_in_milliseconds(self):
        """RTC time in ms, now with real millisecond precision"""
        elapsed = time.monotonic() - self._mono_ref
        secs = self._rtc_ref + elapsed + self.tz_offset
        return int(secs * 1000)

    def append_integer_array_to_delay(self, integer_array, milliseconds: int) :
        if milliseconds < 0:
            return 
        current_time = self.get_local_timestamp_in_milliseconds()
        for integer in integer_array:
            delay_value = IntToDelayValue(integer, current_time + milliseconds)
            self.delays_integer.insert(0, delay_value)

    def append_integer_to_delay(self, integer: int, milliseconds: int) :
        if milliseconds < 0:
            return 
        current_time = self.get_local_timestamp_in_milliseconds()
        delay_value = IntToDelayValue(integer, current_time + milliseconds)
        self.delays_integer.insert(0, delay_value)

    def check_for_integer_to_execute(self) -> list[int]:
        if not self.delays_integer:
            return []

        current_time = self.get_local_timestamp_in_milliseconds()
        ready = []

        array_length = len(self.delays_integer)
        for i in range(array_length - 1, -1, -1):
            delay_value = self.delays_integer[i]
            if delay_value.m_when_to_execute <= current_time:
                ready.append(delay_value.m_integer)
                self.delays_integer.pop(i)
        return ready
