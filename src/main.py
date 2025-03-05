import sys
import os
from STservo_sdk import * # import the STServo SDK library
import Joint

# windows
import re
from usbmonitor import USBMonitor # https://pypi.org/project/usb-monitor/
from usbmonitor.attributes import *
import msvcrt

# linux

def getch():
  return msvcrt.getch().decode()

def getPort():
  if os.name == 'nt':
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
    # import sys, tty, termios
    portname = "/dev/tty.usbserial-*"
  return portname


positions = [0, 45, 90, 180, 225, 270, 315, 360]

def main():
  portname = getPort()

  # Initialize PortHandler instance
  # Set the port path
  # Get methods and members of PortHandlerLinux or PortHandlerWindows
  portHandler = PortHandler(portname)

  if portHandler.openPort():
    print("Succeeded to open the port")
  else:
    print("Failed to open the port")

  # Initialize PacketHandler instance
  # Get methods and members of Protocol
  packetHandler = sts(portHandler)

  serv_motors = [Joint(1, True, packetHandler, 'joint1'),
                 Joint(2, True, packetHandler, 'joint2')]

  for pos in positions:
    for i in range(len(serv_motors)):
      serv_motors[i].writeAngle(pos, 2000, 90)


    # Syncwrite goal position
    sts_comm_result = packetHandler.groupSyncWrite.txPacket()
    if sts_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(sts_comm_result))
    
    # Clear syncwrite parameter storage
    packetHandler.groupSyncWrite.clearParam()
    getch()

  portHandler.closePort()

if __name__ == '__main__':
  main()