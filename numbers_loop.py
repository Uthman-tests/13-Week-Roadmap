for number in range (1,100): # Loop through numbers from 1 to 99
    if number % 5 == 0: # Check if the number is a multiple of 5
        continue # Skip numbers that are multiples of 5
    print(number) # Print the number if it is not a multiple of 5
print('Loop completed.') # Indicate that the loop has finished
