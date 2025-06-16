import random
choices=("r","p","s")
while True:
    user_choice=input("enter the choice:")
    if user_choice not in choices:
        print("invalid input")
        continue
    computer_choice= random.choice(choices)
    print(f"user_choice{user_choice}")
    print(f"computer_choice:{computer_choice}")
    if user_choice==computer_choice:
        print("tie")
    elif user_choice=="r" and computer_choice=="s" or user_choice=="s" and computer_choice=="p" or user_choice=="p" and computer_choice=="r":
        print("you win")
    else:
        print("you loose")
    should_continue=input("enter y/n:").lower()
    if should_continue=="n":
        break