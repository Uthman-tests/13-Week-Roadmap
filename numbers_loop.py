# This loop print numbers from 0-99 exculding the mutiples of 5. 
for number in range (1,100):
    if number % 5 == 0:
        continue
    print(number)
