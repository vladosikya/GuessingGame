import random

GAME = True
while GAME:
    print("Welcome to Guessing Game!")
    print("I will come up with a number from 1 to 100, and you have to guess what number I have in mind.")

    while True:
        level = input("What level of difficulty do you choose? 'easy' or 'hard' ").lower()
        if level == "easy":
            health = 10
            break
        elif level == "hard":
            health = 5
            break
        else:
            print("Unknown command!")

    goal = random.randint(1, 100)
    print(goal)

    while health != 0:
        while True:
            print(f"You have {health} lives.")
            player_answ = input("What number did I guess? ")
            try:
                player_answ = int(player_answ)
                if player_answ == goal:
                    print("Wow, you won. Congratulations :)")
                    health = 0
                    break
                elif player_answ < goal:
                    health -= 1
                    print(f"Wrong. Try a higher number. Health {health}")
                elif player_answ > goal:
                    health -= 1
                    print(f"Wrong. Try a smaller number. Health {health}")
            except:
                print("Need number.")

            if health == 0:
                print("You're lose :(")
                break

    while True:
        choose = input("Do you want to play again? 'y' or 'n' ")
        if choose == 'y':
            break
        elif choose == 'n':
            print("Buy! Buy!")
            GAME = False
            break
        else:
            print("Unknown command.")
