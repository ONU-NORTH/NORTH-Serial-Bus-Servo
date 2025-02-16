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

# sys.path.append("..")
from STservo_sdk import *                 # Uses STServo SDK library

# Default setting
BAUDRATE                    = 1000000           # STServo default baudrate : 1000000
DEVICENAME                  = 'COM5'    # Check which port is being used on your controller
                                                # ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"

joint_list = [1, 2]

# Joint 1
J1_STS_ID                      = 1                 # STServo ID : 1
J1_STS_MINIMUM_POSITION_VALUE  = 0         # STServo will rotate between this value
J1_STS_MAXIMUM_POSITION_VALUE  = 4095         # Max: 4095
J1_STS_MOVING_SPEED            = 1000        # STServo moving speed
J1_STS_MOVING_ACC              = 10          # STServo moving acc

J1_index = 0
J1_sts_goal_position = [J1_STS_MINIMUM_POSITION_VALUE, J1_STS_MAXIMUM_POSITION_VALUE]         # Goal position

# Joint 2
J2_STS_ID                      = 2                 # STServo ID : 1
J2_STS_MINIMUM_POSITION_VALUE  = 0        # STServo will rotate between this value
J2_STS_MAXIMUM_POSITION_VALUE  = 4095         # Max: 4095
J2_STS_MOVING_SPEED            = 1000        # STServo moving speed
J2_STS_MOVING_ACC              = 10          # STServo moving acc

J2_index = 0
J2_sts_goal_position = [J2_STS_MINIMUM_POSITION_VALUE, J2_STS_MAXIMUM_POSITION_VALUE]         # Goal position

# Joint 3
J3_STS_ID                      = 3                 # STServo ID : 1
J3_STS_MINIMUM_POSITION_VALUE  = 0         # STServo will rotate between this value
J3_STS_MAXIMUM_POSITION_VALUE  = 4095         # Max: 4095
J3_STS_MOVING_SPEED            = 1000        # STServo moving speed
J3_STS_MOVING_ACC              = 10          # STServo moving acc

J3_index = 0
J3_sts_goal_position = [J3_STS_MINIMUM_POSITION_VALUE, J3_STS_MAXIMUM_POSITION_VALUE]         # Goal position


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

while 1:
    # for joint in joint_list:
    print("Joint 1:")
    print("Press any key to continue! (or press ESC to quit!)")
    if getch() == chr(0x1b):
        break

    # Write STServo goal position/moving speed/moving acc
    sts_comm_result, sts_error = packetHandler.WritePosEx(J1_STS_ID, J1_sts_goal_position[J1_index], J1_STS_MOVING_SPEED, J1_STS_MOVING_ACC)
    if sts_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(sts_comm_result))
    if sts_error != 0:
        print("%s" % packetHandler.getRxPacketError(sts_error))

    # Change goal position
    if J1_index == 0:
        J1_index = 1
    else:
        J1_index = 0

    print("Joint 2:")
    print("Press any key to continue! (or press ESC to quit!)")
    if getch() == chr(0x1b):
        break

    # Write STServo goal position/moving speed/moving acc
    sts_comm_result, sts_error = packetHandler.WritePosEx(J2_STS_ID, J2_sts_goal_position[J2_index], J2_STS_MOVING_SPEED, J2_STS_MOVING_ACC)
    if sts_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(sts_comm_result))
    if sts_error != 0:
        print("%s" % packetHandler.getRxPacketError(sts_error))

    # Change goal position
    if J2_index == 0:
        J2_index = 1
    else:
        J2_index = 0

    print("Joint 3:")
    print("Press any key to continue! (or press ESC to quit!)")
    if getch() == chr(0x1b):
        break

    # Write STServo goal position/moving speed/moving acc
    sts_comm_result, sts_error = packetHandler.WritePosEx(J3_STS_ID, J3_sts_goal_position[J3_index], J3_STS_MOVING_SPEED, J3_STS_MOVING_ACC)
    if sts_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(sts_comm_result))
    if sts_error != 0:
        print("%s" % packetHandler.getRxPacketError(sts_error))

    # Change goal position
    if J3_index == 0:
        J3_index = 1
    else:
        J3_index = 0

# Close port
portHandler.closePort()
