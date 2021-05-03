# Import necessary modules for OLED
from machine import Pin, I2C
from OLED import SSD1306_I2C
from time import sleep
sleep(1)  # Delay to make OLED actually turn on
# Initialise the I2C bus and OLED display
i2c = I2C(-1, scl=Pin("PB8"), sda=Pin("PB9"))
oled = SSD1306_I2C(128, 64, i2c)

# Print a hello world to the first line of the display
oled.text('Hello, World!', 0, 0)
oled.show()

# Wait
sleep(1)

# Clear the display buffer, removing the hello world
oled.fill(0)

# Print a status string to the second line of the display
oled.text('Enable motors', 0, 10)
oled.show()
sleep(1)

# Clear the display buffer
# Print the value of a variable to the display by formatting a string
dummy_measurement = 123.45
oled_string = "Var = {}"
oled_string.format(dummy_measurement)
oled.text(oled_string)
oled.show()
sleep(1)

# Program ends here