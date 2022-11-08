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

def can_callback(topic_name, msg: HMICanKeyboard_pb2.HmiCanKeyboardState, time):
  print("Button pressed!")
  print(msg)

def brake_cb(topic_name, msg, time):
  print("Brake: {}".format(msg.Signals.is_brake_applied))

def main():
  ecal_core.initialize(sys.argv, "button_demo")

  sub_hmican = ProtoSubscriber("HmiCanKeyboardStatePb", HMICanKeyboard_pb2.HmiCanKeyboardState)
  sub_hmican.set_callback(can_callback)


#  sub_brake = ProtoSubscriber("BrakeInPb", Brake_pb2.Brake)
#  sub_brake.set_callback(brake_cb)

  
  wait_time = 3

  while ecal_core.ok():

    time.sleep(wait_time)
    
  ecal_core.finalize()

if __name__ == "__main__":
  main()
