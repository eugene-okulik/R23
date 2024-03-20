import random

salary = int(input('What is your salary?: '))
bonus = random.choice([True, False])
if bonus:
    salary += random.randint(1, 1000)

print(f'Your salary is: ${salary}')
