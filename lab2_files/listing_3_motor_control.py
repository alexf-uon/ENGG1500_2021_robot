from time import sleep
from motor import Motor

print("Hello, world!")          # Print to REPL at start of program

# Create left and right `Motor' objects
motor_left = Motor("left", "D6", "D7", "D4")

# TODO: Initialise "right" motor

while True:
    motor_left.set_forwards()   # Set the left motor to run forwards
    motor_left.duty(50)         # Set the left motor to 50% pwm
    # TODO: Set the right motor to run forwards at 50% pwm

    sleep(5)                    # Let the motors run forwards for 5 seconds
    motor_left.duty(0)          # Stop the left motor
    # TODO: Stop the right motor
    sleep(5)                    # Let the motors remain stopped for 5 seconds

    # TODO: Set the motor directions to backwards
    # TODO: Set the speed of both motors to full speed
    # TODO: Insert a delay to allow the motors to run backwards for 2.5 seconds before this loop repeats
