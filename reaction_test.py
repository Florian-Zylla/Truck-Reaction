import sys
import time

import ecal.core.core as ecal_core
from ecal.core.subscriber import ProtoSubscriber

from PB.SensorNearData import Brake_pb2

def reaction_test_brake(timeout: int):
    print("Press Brake!")
    sub = ProtoSubscriber("BrakeInPb", Brake_pb2.Brake)

    start_time = ecal_core.getmicroseconds()[1]
    end_time = start_time + 1000*1000 * timeout

    while ecal_core.ok():
        if ecal_core.getmicroseconds()[1] > end_time:
            break
        ret, msg, time = sub.receive(500)
        if msg.signals.is_brake_applied:
            end_time = ecal_core.getmicroseconds()[1]
            break
    score = end_time - start_time
    return score


ecal_core.initialize(sys.argv, "reaction-test")
reaction_test_brake(50)