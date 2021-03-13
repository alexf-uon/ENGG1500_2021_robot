import matplotlib.pyplot as plt
import csv

pwm = []
left_enc = []
right_enc = []

with open('motor_csv.txt','r') as csvfile:
    plotdata = csv.reader(csvfile, delimiter=',')
    for row in plotdata:
            pwm.append(int(row[0]))
            left_enc.append(int(row[1]))
            right_enc.append(int(row[2]))

plt.plot(pwm,left_enc,marker='o')
plt.plot(pwm,right_enc,marker='o')
plt.title("Motor PWM vs Encoder Speed")
plt.xlabel("PWM Duty Cycle")
plt.ylabel("Encoder Count / Speed")
plt.show()

