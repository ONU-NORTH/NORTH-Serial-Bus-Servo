from usbmonitor import USBMonitor
# from usbmonitor.attributes import ID_MODEL, ID_MODEL_ID, ID_VENDOR_ID, ID_USB_INTERFACES
from usbmonitor.attributes import *
import re

# Create the USBMonitor instance
monitor = USBMonitor(filter_devices=({'ID_MODEL':'USB-Enhanced-SERIAL CH343'},{'ID_MODEL_ID':'55D3'}))

# Get the current devices
devices_dict = monitor.get_available_devices()

# Print them
for device_id, device_info in devices_dict.items():
    print(f"{device_id} -- {device_info[ID_MODEL]} ({device_info[ID_MODEL_ID]} - {device_info[ID_VENDOR_ID]})")
    match = re.search(r'\((.*?)\)', device_info[ID_MODEL])
    if match:
      portname = match.group(1)
      print(f"Port: {portname}")


#USB\VID_1A86&PID_55D3\58FD016695 -- USB-Enhanced-SERIAL CH343 (COM5) (55D3 - 1A86)