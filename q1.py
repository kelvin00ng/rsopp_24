# Modeling of the claw machine
# fix the probability of getting the ice cream for the sake of profit 
p = 1/7
n = 10000
import random
data = []
for i in range(n):
    count = 0
    success = False
    while not success:
        count +=1
        success = random.random()<p
    data.append(count)

#print(data)

#sample probability
prob = n/sum(data)
#expected number of tries to get ice cream
suc = 1/prob
print(f'The number of tries before successfully getting the ice cream based on the data is {suc}')