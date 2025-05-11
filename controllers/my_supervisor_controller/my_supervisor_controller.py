"""my_supervisor_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Supervisor

# create the Robot instance.
robot = Supervisor()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

bb8_node = robot.getFromDef('BB-8')
translation_field = bb8_node.getField('translation')

root_node = robot.getRoot()
children = root_node.getField('children')

children.importMFNodeFromString(-1, "DEF BALL Ball { translation 0 1 10 }")
ball_node = robot.getFromDef('BALL')
color = ball_node.getField('color')


i = 0
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.
    if i == 10:
        new_pos = [2.5, 0, 0]
        translation_field.setSFVec3f(new_pos)
    if i == 20:
        bb8_node.remove()
    if i == 30:
        children.importMFNodeFromString(-1, 'Nao { }')

    position = ball_node.getPosition()
    print(position)
    if position[2] < 0.2:
        color.setSFColor([1, 0, 0])

    i += 1

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
