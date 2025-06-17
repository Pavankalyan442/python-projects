import random
while True:
    choice=input("Roll the dice (y/n):")
    if choice=="y" or choice== "Y":
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        print(f"({die1},{die2})")
    elif choice=="n" or choice=="N":
        print("thank you for playing")
        break
    else:
        print("choice is invalid")