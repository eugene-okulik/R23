numbers = list(range(1, 101))
fuzzbuzz = []
for number in numbers:
    if number % 3 == 0 and number % 5 == 0:
        number = 'FuzzBuzz'
        fuzzbuzz.append(number)
    elif number % 5 == 0:
        number = 'Buzz'
        fuzzbuzz.append(number)
    elif number % 3 == 0:
        number = 'Fuzz'
        fuzzbuzz.append(number)
    else:
        fuzzbuzz.append(number)
for items in fuzzbuzz:
    print(items)
