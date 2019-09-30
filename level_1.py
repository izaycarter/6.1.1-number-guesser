from random import randint

random = randint(1,100)

number_of_guess = 0





while number_of_guess != 4:
    print(random)
    guess = int(input("guess my number 1 to 100: "))

    if guess == random:
        print("well aren't you a smarty pants")
        break
    elif guess < random:
        number_of_guess += 1
        print("low balling there buddy")
    elif guess > random:
        number_of_guess += 1
        print("ok there are smaller numbers then that...jeezz")


else:
    print("just...just go home.")
