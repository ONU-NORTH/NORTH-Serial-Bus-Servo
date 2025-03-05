import math as math
from STservo_sdk import *  # import the STServo SDK library

""" motor variables:
    int baudrate_ = 1000000;
    std::string port_ = "/dev/ttyACM0"; // /dev/ttyTHS1 if using UART
    SMS_STS sm_st;
    double KT_ = 9.0; // torque constant (kg*cm / A)
    int steps_ = 4096;
    u16 max_speed_ = 6000; // 6000;
    u8 max_acc_ = 150; // 150;
    """

ST_KT = 9
ST_NUM_STEPS = 4096
ST_MAX_VEL_STEPS = 6000 # steps/second
ST_MAX_ACC_STEPS = 150 # steps/second^2

class Joint:
  def __init__(self, motid, usedeg, packetHandler, jointname):
    self.motid = motid
    self.usedeg = usedeg
    self.packetHandler = packetHandler
    self.jointname = jointname
    

  def writeAngle(self, angle, velocity, accel):
    # convert the passed in angle to a 12-bit value (0 - 4095)
    if self.usedeg:
      servo_angle = math.ceil(angle * (1/360) * ST_NUM_STEPS)
    else:
      servo_angle = math.ceil(angle * 1/(2*math.pi) * ST_NUM_STEPS)

    # sts_comm_result, sts_error = self.packetHandler.WritePosEx(self.motid, servo_angle, 
    #                                                            velocity, accel)
    sts_comm_result, sts_error = self.packetHandler.SyncWritePosEx(self.motid, 
                                                                   servo_angle, velocity, accel)
    
    if sts_comm_result != COMM_SUCCESS:
        print("[ID:%03d]: %s" % (self.motid, 
                                 self.packetHandler.getTxRxResult(sts_comm_result)))
    if sts_error != 0:
        print("[ID:%03d]: %s" % (self.motid, 
                                 self.packetHandler.getRxPacketError(sts_error)))

    


  