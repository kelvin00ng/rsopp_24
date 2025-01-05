
# Modeling of the claw machine
# fix the probability of getting the ice cream
p = 1/6

import random
data = []
for i in range(100):
    count = 0
    success = False
    while not success:
        count +=1
        success = random.random()<p
    data.append(count)

print(data)
