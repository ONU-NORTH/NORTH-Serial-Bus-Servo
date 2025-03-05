#!/usr/bin/env python
#
# *********     Ping Example      *********
#
#
# Available STServo model on this example : All models using Protocol STS
# This example is tested with a STServo and an URT
#

import sys
import os
import re

portname = ""

if os.name == 'nt':
    import msvcrt
    def getch():
        return msvcrt.getch().decode()
    from usbmonitor import USBMonitor # https://pypi.org/project/usb-monitor/
    from usbmonitor.attributes import *

    # Create the USBMonitor instance
    monitor = USBMonitor(filter_devices=({'ID_MODEL':'USB-Enhanced-SERIAL CH343'},{'ID_MODEL_ID':'55D3'}))

    # Get the current devices
    devices = monitor.get_available_devices()

    # Print them
    for device_id, device_info in devices.items():
        print(f"{device_id} -- {device_info[ID_MODEL]} ({device_info[ID_MODEL_ID]} - {device_info[ID_VENDOR_ID]})")
        match = re.search(r'\((.*?)\)', device_info[ID_MODEL])
        if match:
            portname = match.group(1)
            print(f"Port: {portname}")
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
    portname = "/dev/tty.usbserial-*"

# sys.path.append("..")
from STservo_sdk import *                   # Uses STServo SDK library

# Servo settings
SERVOLIST               = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
BAUDRATE                = 1000000           # STServo default baudrate : 1000000
DEVICENAME              = portname

# Initialize PortHandler instance
# Set the port path
# Get methods and members of PortHandlerLinux or PortHandlerWindows
portHandler = PortHandler(DEVICENAME)

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

# for id in STS_ID:
    # Try to ping the STServo
    # Get STServo model number
    # sts_model_number, sts_comm_result, sts_error = packetHandler.ping(id)

for id in SERVOLIST:
    print("Pinging servo: [ID:%03d]" % (id))
    sts_model_number, sts_comm_result, sts_error = packetHandler.ping(id)

    if sts_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(sts_comm_result))
    else:
        # print("[ID:%03d] ping Succeeded. STServo model number : %d" % (id, sts_model_number))
        print("[ID:%03d] ping Succeeded. STServo model number : %d" % (id, sts_model_number))

    # if sts_error != 0:
        # print("%s" % packetHandler.getRxPacketError(sts_error))

# Close port
portHandler.closePort()