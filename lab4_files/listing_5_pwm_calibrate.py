# TODO: Import necessary modules
# TODO: Initialise encoders
# TODO: Initialise motors

print("PWM, ENC_L, ENC_R");

while True:
  pwm = 0;
  for pwm in range(0,100,5) #Loop from 0-100% increasing by 5%
    # TODO:
    # Zero encoders
    # Set left and right motor PWM
    # Sleep for 1 second

    # Read the encoders
    left_count = enc.get_left()
    right_count = enc.get_right()
    # Print pwm and encoder values to the serial monitor in CSV format:
    print("{:3d}, {:4d}, {:4d}".format(pwm, left_count, right_count))