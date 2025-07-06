print('Enter your grades for the following subjects:')
subjects = ['Math', 'Computer', 'English', 'History', 'Arts']
grades = {}
for topic in subjects:
    while True:
        try:
            grade = float(input(f'Enter your grade for {topic}: '))
            if grade >= 90 and grade <= 100:
                print('You got an A.')
            elif grade >=80 and grade <= 89.99:
                print('You got a B.')
            elif grade >= 70 and grade <= 79.99:
                print('You got a C.')
            elif grade >= 60 and grade <= 69.99:
                print('You got a D.')
            elif grade >= 0 and grade <= 59.99:
                  print('You got an F.')
            else:
                print('Invalid grade. Please enter a number between 0 and 100.')
                continue
            grades[topic] = grade
            break
        except ValueError:
            print('Invalid input. Please enter a valid number.')    
