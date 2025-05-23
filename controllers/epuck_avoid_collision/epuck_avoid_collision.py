"""epuck_avoid_collision controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, DistanceSensor, Motor

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

ps = []
ps_names = [
    'ps0', 'ps1', 'ps2', 'ps3',
    'ps4', 'ps5', 'ps6', 'ps7'
]

for i in range(len(ps_names)):
    ps.append(robot.getDevice(ps_names[i]))
    ps[i].enable(timestep)
    
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

MAX_SPEED = 6.28

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)
loop_count = 0
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.
    ps_values = []
    for i in range(len(ps_names)):
        ps_values.append(ps[i].getValue())
    if loop_count % 100 == 0:
        print(ps_values)
        
    right_obstacle = ps_values[0] > 80.0 or ps_values[1] > 80.0 or ps_values[2] > 80.0
    left_obstacle = ps_values[5] > 80.0 or ps_values[6] > 80.0 or ps_values[7] > 80.0
    
        
    left_speed = 0.5 * MAX_SPEED
    right_speed = 0.5 * MAX_SPEED
    
    if left_obstacle:
        left_speed = 0.5 * MAX_SPEED
        right_speed -= 0.5 * MAX_SPEED
    elif right_obstacle:
        left_speed -= 0.5 * MAX_SPEED
        right_speed = 0.5 * MAX_SPEED
    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    loop_count += 1
    pass

# Enter here exit cleanup code.
