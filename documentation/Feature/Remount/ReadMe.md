
```
import storage
import usb_cdc
import usb_hid
import usb_midi

# Activer toutes les interfaces USB (facultatif mais utile)
usb_cdc.enable(console=True, data=True)
usb_hid.enable((usb_hid.Device.KEYBOARD, usb_hid.Device.MOUSE))
usb_midi.enable()

# Monte le disque CIRCUITPY en lecture/écriture
storage.remount("/", readonly=False)

# Active le disque USB (rends-le visible par ton PC)
storage.enable_usb_drive()
```
