# Declare states
state_list = ['DRIVING', 'FOLLOW_LEFT_WALL', 'FOLLOW_RIGHT_WALL', 'STOPPED']

state = 'DRIVING'   # Default state on init is DRIVING
start_time = millis()

# Initialise variables
dir_left  = 0
dir_right = 0
pwm_left  = 0
pwm_right = 0

while True:
    # Collect sensor data
    time = elapsed_millis(start_time)
    sonar_dist = ultrasonic_sensor.distance_mm()
    # TODO: Read value from line sensor
    #(Use analog or binary value, your decision as a team)
    line_measurement_1 = ???


  # Make decisions according to state machine
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
        if ():# TODO: condition based on measurement here:
            state = 'FOLLOW_LEFT_WALL'
        elif ():# TODO: condition based on measurement here:
            state = 'FOLLOW_RIGHT_WALL'
        else:
            state = state
    
    elif state == 'FOLLOW_LEFT_WALL':
        print(state)         # Update to OLED
        # Actions
        # TODO: Drive by setting direction and PWM values according to distance

        # Transition condition
        if (): # TODO: condition based on measurement here
            state = 'STOPPED'
        else:
            state = state


    elif state == 'FOLLOW_RIGHT_WALL':
        print(state)         # Update to OLED
        # Actions
        # TODO: Drive by setting direction and PWM values according to distance

        # Transition condition
        if (): # TODO: condition based on measurement here
            state = 'STOPPED'
        else:
            state = state

    elif state == 'STOPPED':
        print(state)         # Update to OLED
        # Actions
        # TODO: Stop driving, by setting dir and pwm values 
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
