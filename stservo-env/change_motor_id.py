#!/usr/bin/env python
#
# *********     Gen Write Example      *********
#
#
# Available STServo model on this example : All models using Protocol STS
# This example is tested with a STServo and an URT
#

import sys
import os
import struct
from usbmonitor import USBMonitor
from usbmonitor.attributes import *
import re
sys.path.append("..")
from STservo_sdk import *                 # Uses STServo SDK library

# Create the USBMonitor instance
monitor = USBMonitor(filter_devices=({'ID_MODEL':'USB-Enhanced-SERIAL CH343'},{'ID_MODEL_ID':'55D3'}))

# Get the current devices
devices_dict = monitor.get_available_devices()

# Print them
for device_id, device_info in devices_dict.items():
    # print(f"{device_id} -- {device_info[ID_MODEL]} ({device_info[ID_MODEL_ID]} - {device_info[ID_VENDOR_ID]})")
    match = re.search(r'\((.*?)\)', device_info[ID_MODEL])
    if match:
      portname = match.group(1)
      print(f"Port: {portname}")

if os.name == 'nt':
    import msvcrt
    def getch():
        return msvcrt.getch().decode()
        
else:
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


# Default setting
STS_ID_CHANGE_FROM = 1 # STServo ID : 1
STS_ID_CHANGE_TO   = 5
BAUDRATE           = 1000000           # STServo default baudrate : 1000000
SMS_STS_ID         = 5  # DO NOT CHANGE THIS (serial cmd to change the device id)

# Initialize PortHandler instance
# Set the port path
# Get methods and members of PortHandlerLinux or PortHandlerWindows
portHandler = PortHandler(portname)

# Initialize PacketHandler instance
# Get methods and members of Protocol
packetHandler = sts(portHandler)
    
# Open port
if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    print("Press any key to terminate...")
    getch()
    quit()

# Set port baudrate
if portHandler.setBaudRate(BAUDRATE):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    print("Press any key to terminate...")
    getch()
    quit()


id_bytes = STS_ID_CHANGE_TO.to_bytes(1, 'big')

packetHandler.unLockEprom(STS_ID_CHANGE_FROM)
sts_comm_result, sts_error = packetHandler.writeTxRx(STS_ID_CHANGE_FROM, SMS_STS_ID, 1, id_bytes); #ID

# error handling
if sts_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(sts_comm_result))
if sts_error != 0:
    print("%s" % packetHandler.getRxPacketError(sts_error))

print("%s" % packetHandler.getTxRxResult(sts_comm_result)); #ID

packetHandler.LockEprom(STS_ID_CHANGE_TO); # EPROM-SAFE locked

print("Successfully changed motor id from [ID:%03d] to [ID:%03d]" % (STS_ID_CHANGE_FROM, STS_ID_CHANGE_TO))

portHandler.closePort()