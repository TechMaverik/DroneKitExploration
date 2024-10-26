"""AutoPilot_Takeoff_Landing"""

from dronekit import connect, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--connect", default="127.0.0.1:14550")
args = parser.parse_args()

# Connect to the Vehicle
print("*** AutoPilot_Takeoff_Landing ***")
print("[ *** Connecting to Drone on: %s ***]" % args.connect)
vehicle = connect(args.connect, baud=921600, wait_ready=True)
# 921600 is the baudrate that you have set in the mission planner or QGC


# Function to arm and then takeoff to a user-specified altitude
def arm_and_takeoff(aTargetAltitude):
    print("Basic pre-arm checks ...")
    # Don't let the user try to arm until autopilot is ready
    while not vehicle.is_armable:
        print(" Waiting for Drone to initialise...")
        time.sleep(1)

    print("Arming motors")
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude)  # Take off to target altitude

    # Check that vehicle has reached takeoff altitude
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        # Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)


# Initialize the takeoff sequence to 15m
arm_and_takeoff(15)

print("*** Taking off Completed ***")

# Hover for 10 seconds
time.sleep(15)

print("Landing Initiated ...")
vehicle.mode = VehicleMode("LAND")

# Close vehicle object
vehicle.close()
