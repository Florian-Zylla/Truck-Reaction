import sys
import random
import time

import ecal.core.core as ecal_core
from ecal.core.subscriber import ProtoSubscriber

from PB.SensorNearData import Brake_pb2
from PB.SensorNearData import VehicleDynamics_pb2


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

def reaction_left_steering(timeout: int):
    print("Steer left!")
    sub = ProtoSubscriber("VehicleDynamicsInPb", VehicleDynamics_pb2.VehicleDynamics)

    start_time = ecal_core.getmicroseconds()[1]
    end_time = start_time + 1000*1000 * timeout

    while ecal_core.ok():
        if ecal_core.getmicroseconds()[1] > end_time:
            break
        ret, msg, time = sub.receive(500)
        if msg.signals.steering_wheel_angle > 0.2:
            end_time = ecal_core.getmicroseconds()[1]
            break
    score = end_time - start_time
    return score


def reaction_right_steering(timeout: int):
    print("Steer right!")
    sub = ProtoSubscriber("VehicleDynamicsInPb", VehicleDynamics_pb2.VehicleDynamics)

    start_time = ecal_core.getmicroseconds()[1]
    end_time = start_time + 1000*1000 * timeout

    while ecal_core.ok():
        if ecal_core.getmicroseconds()[1] > end_time:
            break
        ret, msg, time = sub.receive(500)
        if msg.signals.steering_wheel_angle < -0.2:
            end_time = ecal_core.getmicroseconds()[1]
            break
    score = end_time - start_time
    return score

def ms_to_score(time):
    time_ms = time / 1000.
    return time_ms / 100

ecal_core.initialize(sys.argv, "reaction-test")
# print("Score brake: {}".format(ms_to_score(reaction_test_brake(50))))
# print("Score left:  {}".format(ms_to_score(reaction_left_steering(50))))
# print("Score right: {}".format(ms_to_score(reaction_right_steering(50))))

total_score = 0
max_timeout = 50 # seconds
max_wait = 10 # seconds
min_wait = 2 # seconds
while True:
    print("Total Score: {}\n\n".format(total_score))
    test = random.randint(0, 2)
    wait = random.random() * max_wait
    wait = max(min_wait, wait)
    time.sleep(wait)

    score = max_timeout
    test_name = "Error"
    if test == 0:
        score = ms_to_score(reaction_test_brake(max_timeout))
        test_name = "Braking Test"
    elif test == 1:
        score = ms_to_score(reaction_right_steering(max_timeout))
        test_name = "Right Steering Test"
    elif test == 2:
        score = ms_to_score(reaction_left_steering(max_timeout))
        test_name = "Left Steering Test"
    print("{} - Score: {}".format(test_name, score))
    total_score += score
