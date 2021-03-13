# Distances from the centroid of the robot to the centre of each sensor in mm 
x1 = -22.5;
x2 = -7.5;
x3 = 7.5;
x4 = 22.5;

# Initialise pins for analog line sensors
adc_A1 = ADC(Pin("A1"))
adc_A2 = ADC(Pin("A2"))
adc_A3 = ADC(Pin("A3"))
adc_A4 = ADC(Pin("A4"))

while True:
  #   TODO: Take sensor measurements using "w1 = adc_A1.read()" 
  #         storing sensor data in w1, w2, w3, w4
  #   TODO: Calculate numerator of weighted average
  numerator = ???
  #   TODO: Calculate denominator of weighted average
  denominator = ???

  line_dist = numerator/denominator;

  print("Distance from line = {:3.2f}".format(line_dist));
  sleep(0.1);  #   50ms delay
