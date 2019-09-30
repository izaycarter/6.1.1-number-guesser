from random import randint

number_of_guess = 0

number = int(input("pick a number between 1 and 100.. bet i can guess it: "))
high = 100
low = 1

guess = (high + low) // 2

while number_of_guess < 5:
    number_of_guess += 1
    print(guess)
    if guess < number:
        low = guess
        guess = randint(low,high)

    elif guess > number:
        high = guess
        guess = randint(low,high)

    elif guess == number:
        print("BOOM! your number is: "+number)
        break
else:
    print("at least i dont have bills...")
