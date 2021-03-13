import matplotlib.pyplot as plt
import csv

apds9960 = []
ultrasonic = []

with open('distance_csv.txt','r') as csvfile:
    plotdata = csv.reader(csvfile, delimiter=',')
    for row in plotdata:
        apds9960.append(int(row[0]))
        ultrasonic.append(int(row[1]))

plt.plot(ultrasonic,apds9960,marker='o')
plt.title("APDS9960 vs Ultrasonic Sensor")
plt.xlabel("Ultrasonic distance [mm]")
plt.ylabel("APDS9960 distance [no units]")
plt.show()

