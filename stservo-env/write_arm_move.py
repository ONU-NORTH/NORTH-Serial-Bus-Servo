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

def write_position(motor_id, goal_pos, speed, accel):
    sts_comm_result, sts_error = packetHandler.WritePosEx(motor_id, motor_id, speed, accel)
    if sts_comm_result != COMM_SUCCESS:
        print("[ID:%03d]: %s" % (motor_id, packetHandler.getTxRxResult(sts_comm_result)))
    if sts_error != 0:
        print("[ID:%03d]: %s" % (motor_id, packetHandler.getRxPacketError(sts_error)))


# joint_list = [1, 2]

# Joints
Joint_STS_ID_list         = [1, 2, 3, 4, 5]
Joint_MIN_POSITION_VALUE  = 0         # STServo will rotate between this value
Joint_MAX_POSITION_VALUE  = 4095         # Max: 4095
STS_MOVING_SPEED        = 2000        # STServo moving speed
STS_MOVING_ACC          = 100          # STServo moving acc

index = 0
sts_goal_position = [[Joint_MIN_POSITION_VALUE, Joint_MAX_POSITION_VALUE],
                     [Joint_MAX_POSITION_VALUE, Joint_MIN_POSITION_VALUE],
                     [Joint_MIN_POSITION_VALUE, Joint_MAX_POSITION_VALUE],
                     [Joint_MAX_POSITION_VALUE, Joint_MIN_POSITION_VALUE],
                     [Joint_MIN_POSITION_VALUE, Joint_MAX_POSITION_VALUE]]         # Goal position

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
    # print("Joint 1:")
    # print("Press any key to continue! (or press ESC to quit!)")
    # if getch() == chr(0x1b):
    #     break
    

    # Write STServo goal position/moving speed/moving acc
    # sts_comm_result, sts_error = packetHandler.WritePosEx(J1_STS_ID, J1_sts_goal_position[J1_index], J1_STS_MOVING_SPEED, J1_STS_MOVING_ACC)
    # if sts_comm_result != COMM_SUCCESS:
    #     print("%s" % packetHandler.getTxRxResult(sts_comm_result))
    # if sts_error != 0:
    #     print("%s" % packetHandler.getRxPacketError(sts_error))

    for mot_id in Joint_STS_ID_list:
        sts_addparam_result = packetHandler.SyncWritePosEx(mot_id, sts_goal_position[mot_id - 1][index], STS_MOVING_SPEED, STS_MOVING_ACC)
        if sts_addparam_result != True:
            print("[ID:%03d] groupSyncWrite addparam failed" % mot_id)

    # sts_comm_result = packetHandler.SyncWritePosEx(1, 2075, 1000, 50);    
    # if sts_comm_result != COMM_SUCCESS:
    #     print("%s" % packetHandler.getTxRxResult(sts_comm_result))
    # time.sleep(10)

    # Syncwrite goal position
    sts_comm_result = packetHandler.groupSyncWrite.txPacket()
    if sts_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(sts_comm_result))
    
    # Clear syncwrite parameter storage
    packetHandler.groupSyncWrite.clearParam()

    # print("Position: %03d" % packetHandler.ReadPos(1))

    # while packetHandler.ReadPos(1) != sts_goal_position[1][index]:
    #     time.sleep(1)

    # Change goal position
    if index == 0:
        index = 1
    else:
        index = 0
        
    time.sleep(5)
# Close port
portHandler.closePort()