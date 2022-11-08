"""
Copyright (c) 2022 Continental Autonomous Mobility Germany GmbH
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import sys
import time

import ecal.core.core as ecal_core
from ecal.core.subscriber import ProtoSubscriber

from PB.HMI import HMICanKeyboard_pb2
from PB.SensorNearData import Brake_pb2
from PB.SensorNearData import VehicleDynamics_pb2

class eCAL_Interface:
  pass

eCAL_Command = eCAL_Interface()


eCAL_Command.brake = 42 # 0 = off,  1= on, 42 = init
eCAL_Command.steering = 0 # 0= init, 0.4 = left_max, -0.4 = right_max
eCAL_Command.steering_tux = 42 #42 = init, 0= neutral, 1 = left, -1 = right


def can_callback(topic_name, msg: Brake_pb2.Brake, time):


  print("Brake pressed!")
  print(msg)

def brake_cb(topic_name, msg, time):
  global eCAL_Command
  if msg.signals.is_brake_applied == True:
      #print("Break active")
      eCAL_Command.brake = 1
  else:
      #print("Break off")
      eCAL_Command.brake = 0

def steering_cb(topic_name, msg , time):
  global eCAL_Command
  eCAL_Command.steering = msg.signals.steering_wheel_angle


def main():
  ecal_core.initialize(sys.argv, "button_demo")

  #sub_hmican = ProtoSubscriber("HmiCanKeyboardStatePb", HMICanKeyboard_pb2.HmiCanKeyboardState)
  #sub_hmican.set_callback(can_callback)
  sub_brake = ProtoSubscriber("BrakeInPb", Brake_pb2.Brake)
  sub_brake.set_callback(brake_cb)
  sub_steering = ProtoSubscriber("VehicleDynamicsInPb", VehicleDynamics_pb2.VehicleDynamics)
  sub_steering.set_callback(steering_cb)
  
  wait_time = 0.5

  while ecal_core.ok():

    time.sleep(wait_time)
    print(eCAL_Command.brake, eCAL_Command.steering)
    
  ecal_core.finalize()

if __name__ == "__main__":
  main()
