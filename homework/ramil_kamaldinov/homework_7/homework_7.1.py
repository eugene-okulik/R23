while True:
    user_input = int(input('Guess the number: '))
    if user_input != 23:
        print('Try again')
    else:
        print('Congratulations! You guessed it right!')
        break
