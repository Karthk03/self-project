numbers = [0,0,0,0,0,0]
import random
import time

for i in range(6):
    numbers[i] = random.randint(10,100)
    print(numbers[i])

initalTime = time.time()

sum = 0
for i in numbers:
    sum+=i

sumInput = input('what is the sum?: ')
if(sum == int(sumInput)):
    print('you got it right!')
else:
    print('you made a mistake the correct answer is:'+str(sum))

timeTaken = time.time()-initalTime
print('time taken is: '+str(timeTaken))
