from machine import SoftI2C, Pin
from time import sleep
from APDS9960LITE import APDS9960LITE
# TODO: Import ultrasonic sensor module

# Initialise I2C bus
i2c = SoftI2C(scl=Pin("PB13"), sda=Pin("PB14"))
# Initialise APDS9660
apds9960=APDS9960LITE(i2c)      # Create APDS9660 sensor object
apds9960.prox.enableSensor()    # Send I2C command to enable sensor
sleep(0.1)  # Let sensor measurment stabilise before starting loop

# TODO: Initialise the ultrasonic sensor

for i in range(100):  # Take 100 measurements
    proximity_measurement = apds9960.prox.proximityLevel  # Read the proximity value
    ultrasonic_measurement_mm = 1.0 # TODO: Read the ultrasonic sensor instead of always 1.0
    print("{:3d}, {:4.2f}".format(proximity_measurement,ultrasonic_measurement_mm))
    sleep(0.2)  # Wait for measurement to be ready

print("Experiment finished! Please restart processor to repeat.")