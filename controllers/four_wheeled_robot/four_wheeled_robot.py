"""four_wheeled_robot controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor
from controller.device import Device

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

wheels: list[Device] = []
wheels_names = ["wheel_lf", "wheel_rf", "wheel_rb", "wheel_lb"]
for name in wheels_names:
    print(f"name={name}")
    d = robot.getDevice(name)
    wheels.append(d)
    d.setPosition(float("inf"))
    d.setVelocity(0.0)


ds_list: list[Device] = []
ds_names = ['ds_right', 'ds_left']
for name in ds_names:
    print(f"name={name}")
    d = robot.getDevice(name)
    d.enable(1)
    ds_list.append(d)

avoid_obstacle_counter = 0

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.
    left_speed = 1.0
    right_speed = 1.0
    if avoid_obstacle_counter > 0:
        avoid_obstacle_counter -= 1
        left_speed = 1.0
        right_speed = -1.0
    else:
        for ds in ds_list:
            if ds.getValue() < 950.0:
                avoid_obstacle_counter = 100
    wheels[0].setVelocity(left_speed)
    wheels[3].setVelocity(left_speed)
    wheels[1].setVelocity(right_speed)
    wheels[2].setVelocity(right_speed)


    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
