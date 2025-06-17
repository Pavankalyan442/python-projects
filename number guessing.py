import random
number_to_guess=random.randint(1,100)
while True:
    try:
        guess=int(input("enter the number from 1 to 100:"))
    except ValueError:
        print("enter valid number")

    
    if guess>number_to_guess:
        print("number is too high")
    elif guess<number_to_guess:
        print("number is too low")
    else:
        print("congrats you have guessed the number")
        break
    
    