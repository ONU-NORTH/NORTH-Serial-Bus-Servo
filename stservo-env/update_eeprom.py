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

sys.path.append("..")
from STservo_sdk import *                 # Uses STServo SDK library

# Default setting
STS_ID_CHANGE_FROM = 1 # STServo ID : 1
STS_ID_CHANGE_TO   = 4
BAUDRATE                    = 1000000           # STServo default baudrate : 1000000
DEVICENAME                  = 'COM5'    # Check which port is being used on your controller
                                                # ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"
SMS_STS_ID = 5

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


id_bytes = STS_ID_CHANGE_TO.to_bytes(1, 'big')

packetHandler.unLockEprom(STS_ID_CHANGE_FROM)
sts_comm_result, sts_error = packetHandler.writeTxRx(STS_ID_CHANGE_FROM, SMS_STS_ID, 1, id_bytes); #ID
print("%s" % packetHandler.getTxRxResult(sts_comm_result)); #ID
packetHandler.LockEprom(STS_ID_CHANGE_TO); # EPROM-SAFE locked

portHandler.closePort()
