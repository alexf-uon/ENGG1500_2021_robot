from pyb     import millis, elapsed_millis
from machine import Pin
from time    import sleep
from motor   import Motor
import ultrasonic

# TODO: Ensure these are the pin numbers used on your robot
ECHO  = "D12"
TRIG  = "D13"
LINE1 = "INTENTIONALLY_UNDEFINED_PIN_ERROR" # TODO: Insert line sensor pin
# Initialise the motors
motor_left  = Motor("left", "D6", "D7", "D4")
motor_right = Motor("right", "D8", "D9", "D5")
# Initialise the ultrasonic sensor
ultrasonic_sensor = ultrasonic.HCSR04(ECHO, TRIG)
# Initialise a line sensor
line_sensor_1 = Pin(LINE1, Pin.IN)

# Declare variables that need to retain value in loop
pwm_left  = 0
pwm_right = 0
dir_left  = 0
dir_right = 0

# Declare states
state_list = ['DRIVING', 'FOLLOW_WALL', 'STOPPED']

state = 'DRIVING'   # Default state on init is DRIVING
start_time = millis()

while True:
    # Collect sensor data
    time = elapsed_millis(start_time)
    sonar_dist = ultrasonic_sensor.distance_mm()
    # TODO: Read value from line sensor
    #(Use analog or binary value, your decision as a team)
    line_measurement_1 = ???

    # TODO: State machine here
    if state == 'DRIVING':
        print(state)         # Update to OLED
        # Actions
        # TODO: Drive by setting direction and PWM values
        dir_left  = #???
        dir_right = #???
        pwm_left  = #???
        pwm_right = #???
        # Transition condition
        if ():  # TODO: Condition based on measurement here
            state = 'FOLLOW_WALL'
        else:
            state = state  # Remain in current state if condition not met

    elif state == 'FOLLOW_WALL':
        print(state)         # Update to OLED
        # Actions
        # TODO: Drive by setting direction and PWM values according to distance

        # Transition condition
        if ():  # TODO: Condition based on measurement here
            state = 'STOPPED'
        else:
            state = state  # Remain in current state if condition not met

    elif state == 'STOPPED':
        print(state)         # Update to OLED
        # Actions
        # TODO: Stop driving by setting PWM values
        dir_left  = 'back' # Trollolol
        dir_right = 'back' # Trollolol
        pwm_left  = 70     # Trollolol
        pwm_right = 70     # Trollolol
        # No transition condition, remain in a safe state.

    else:
        print('Incorrect state selected!') # Update to OLED

    # Finally, send control signals to motors
    if dir_left == 'fwd':
        motor_left.set_forwards()
    else:
        motor_left.set_backwards()
    if dir_right == 'fwd':
        motor_right.set_forwards()
    else:
        motor_right.set_backwards()

    motor_left.duty(pwm_left)
    motor_right.duty(pwm_right)

    time.sleep(0.02)
