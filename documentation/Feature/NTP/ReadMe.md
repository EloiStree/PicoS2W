


```
import time
import wifi
import socketpool
import adafruit_ntp
import rtc

======== WiFi Credentials ========
WIFI_SSID = "YourWiFiName"
WIFI_PASSWORD = "YourWiFiPassword"

======== Connect to WiFi ========
print("Connecting to WiFi...")
wifi.radio.connect(WIFI_SSID, WIFI_PASSWORD)
print("Connected to", WIFI_SSID)
print("IP address:", wifi.radio.ipv4_address)

======== Create Socket Pool ========
pool = socketpool.SocketPool(wifi.radio)

======== Connect to NTP Server ========
print("Querying NTP server...")
ntp = adafruit_ntp.NTP(pool, server="pool.ntp.org", tz_offset=0)  # UTC

======== Get NTP Time ========
ntp_time = ntp.datetime  # returns struct_time
ntp_unix = time.mktime(ntp_time)  # convert to seconds since epoch

======== Get Local Device Time ========
local_unix = time.time()  # local time (seconds since epoch)

======== Calculate Difference ========
difference_ms = int((ntp_unix - local_unix) * 1000)
print("NTP time (UTC):", time.localtime(ntp_unix))
print("Local device time:", time.localtime(local_unix))
print("Time difference:", difference_ms, "ms")

======== Optionally Set RTC to NTP Time ========
rtc.RTC().datetime = ntp_time
print("RTC updated with NTP time.")

```
