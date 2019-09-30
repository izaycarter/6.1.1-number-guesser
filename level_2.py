from random import randint



user_number = input("pick a number 1 through 100 and ill see if i can guess it: ")

user = int(user_number)

guess = 0

while guess <= 4:
    computer = randint(1,100)
    if computer == user:
        print("boom roast your number is: ",user )
        break
    else:
        print("dang it")
        guess += 1


else:
    print("your lucky im stuck in this sreen...")
