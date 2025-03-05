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

def constrain(val, min_range, max_range):
  """ constrain:
      keeps a number withinn a range of values, prevents a number being larger than whats expected
      :param val: the value to be constrained
      :param min_range: the smallest number that val can be, if lower return min_range, otherwise return val
      :param max_range: the largest number that val can be, if higher return max_range, otherwise return val
  """
  return min(max_range, max(min_range, val))

class Joint(object):
  def __init__(self, packetHandler, motid, jointname, usedeg):
    self.packetHandler = packetHandler
    self.motid = motid
    self.jointname = jointname
    self.usedeg = usedeg
    self.joint_min_pos_steps = 0 
    self.joint_max_pos_steps = ST_NUM_STEPS
    self.midpoint_pos_steps = math.ceil(ST_NUM_STEPS / 2)

  def angle2Steps(self, angle):
    # convert the passed in angle to a 12-bit value (0 - 4095)
    if self.usedeg:
      return math.ceil(angle * (1/360) * ST_NUM_STEPS)
    else:
      return math.ceil(angle * (1/(2*math.pi)) * ST_NUM_STEPS)
  
  # this needs to be double checked (need to figure out the math on this conversion), not sure this is correct
  def velocty2Steps(self, velocity):
    # convert the passed in velocity (expressed in deg/sec or rad/s) to a steps/second value
    if self.usedeg:
      return min(math.ceil(velocity * (1/360) * ST_NUM_STEPS), ST_MAX_VEL_STEPS)
    else:
      return min(math.ceil(velocity * (1/(2*math.pi)) * ST_NUM_STEPS), ST_MAX_VEL_STEPS)


  def setJointRange(self, min_pos, max_pos, midpoint_pos):
    self.joint_min_pos_steps = self.angle2Steps(min_pos)
    self.joint_max_pos_steps = self.angle2Steps(max_pos)
    self.midpoint_pos_steps = self.angle2Steps(midpoint_pos)

  def writeAngle(self, angle, velocity, accel):
    servo_angle_steps = self.angle2Steps(angle)
    # servo_velocity_steps = self.angle2Steps(velocity)
    # servo_accel_steps = self.angle2Steps(accel)

    # make sure servo_angle_steps doesnt go outside the physical capabilities of that joint
    servo_angle_steps = constrain(servo_angle_steps, 
                                  self.joint_min_pos_steps, self.joint_max_pos_steps)
                           

    # sts_comm_result, sts_error = self.packetHandler.WritePosEx(self.motid, servo_angle, 
    #                                                            velocity, accel)

    addparam_result = self.packetHandler.SyncWritePosEx(self.motid, servo_angle_steps, velocity, accel)
  
    if addparam_result != True:
      print("[Joint: %6s ID:%03d] groupSyncWrite addparam failed" % (self.jointname, self.motid))

    


  