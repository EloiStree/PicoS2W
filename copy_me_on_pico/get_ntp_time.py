import time
import rtc
import adafruit_ntp
import socketpool
import wifi


class GetNtpUtcTimestampTimeAndDifference:
    def __init__(self, server_address="pool.ntp.org", tz_offset=0):
        self.tz_offset = tz_offset
        pool = socketpool.SocketPool(wifi.radio)

        try:
            self.ntp = adafruit_ntp.NTP(pool, server=server_address)
        except Exception as e:
            print("NTP init failed:", e)
            self.ntp = None

        self.rtc = rtc.RTC()

        # sync RTC + set monotonic reference
        self.sync_rtc_to_ntp()

    def sync_rtc_to_ntp(self):
        """Set the RTC from NTP time & reset fractional timer"""
        try:
            if self.ntp is not None:
                self.rtc.datetime = self.ntp.datetime
                print("RTC synced to NTP.")
            else:
                raise RuntimeError("NTP unavailable")

        except Exception as e:
            print("RTC sync failed, offset set to 0:", e)
            self.tz_offset = 0

        # always set monotonic refs so functions still work
        self._mono_ref = time.monotonic()
        self._rtc_ref = time.time()

    def get_local_timestamp_in_milliseconds(self):
        """RTC time in ms, now with real millisecond precision"""
        elapsed = time.monotonic() - self._mono_ref
        secs = self._rtc_ref + elapsed + self.tz_offset
        return int(secs * 1000)

    def get_ntp_utc_timestamp_in_milliseconds(self):
        """NTP UTC time in ms — offset resets to 0 if this errors"""
        try:
            secs = time.mktime(self.ntp.datetime) + self.tz_offset
            return int(secs * 1000)

        except Exception as e:
            print("NTP read failed, offset set to 0:", e)
            self.tz_offset = 0
            secs = time.time()
            return int(secs * 1000)

    def get_local_to_ntp_utc_difference_milliseconds(self):
        """Drift of RTC vs true NTP (ms)"""
        return (
            self.get_ntp_utc_timestamp_in_milliseconds()
            - self.get_local_timestamp_in_milliseconds()
        )
