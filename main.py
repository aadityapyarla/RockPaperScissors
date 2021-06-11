import random
print("Welcome To Rock, Paper and Scissors, It's a 3 point game")
print("Simply type rock (or) paper (or) scissors (or) quit")
user = ""
user_points = 0
system_points = 0

while user != "quit":
    user = input("> ").lower()
    system = random.choice(["rock", "paper", "scissors"])

    if user == system:
        print(system)
        print("  You  Computer  ")
        print(f"   {user_points}       {system_points}")

    elif user == "rock" or user == "paper" or user == "scissors":
        print(system)
        if (user == "rock" and system == "scissors") or (user == "scissors" and system == "paper") or\
                (user == "paper" and system == "rock"):
            user_points += 1
            print("  You  Computer  ")
            print(f"  {user_points}       {system_points}")
        elif (system == "rock" and user == "scissors") or (system == "scissors" and user == "paper") or \
                (system == "paper" and user == "rock"):
            system_points += 1
            print("  You  Computer  ")
            print(f"   {user_points}       {system_points}")

    elif user == "quit":
        print("Thank You for Playing!")
        break
    elif user != "quit" and user != "rock" and user != "paper" and user != "scissors" and user != "y" and user != "n":
        print("I didn't understand")

    if user_points == 3 or system_points == 3:
        if user_points == 3 and system_points != 3:
            print("Congrats! You win..")
            print("Wanna play again? (y/n)")
            user_1 = input("> ")
            if user_1 == "y":
                user_points = 0
                system_points = 0
            elif user_1 == "n":
                print("Thank You for Playing!")
                break
        elif system_points == 3 and user_points != 3:
            print("Sorry! You lose..")
            print("Wanna play again? (y/n)")
            user_2 = input("> ")
            if user_2 == "y":
                user_points = 0
                system_points = 0
            elif user_2 == "n":
                print("Thank You for Playing!")
                break


