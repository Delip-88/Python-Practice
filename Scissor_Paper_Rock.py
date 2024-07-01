import random

print("SCISSOR, PAPER, ROCK GAME. BEST OF THREE")
options = {
    1: 'scissor',
    2: 'paper',
    3: 'rock'
}

user_point = 0
com_point = 0

while user_point < 3 and com_point < 3:
    try:
        user_choice = int(input(f"Choose an option {options}: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if user_choice in options.keys():
        com_choice = random.choice(list(options.keys()))
        
        print(f"You chose: {options.get(user_choice)}")
        print(f"Computer chose: {options.get(com_choice)}")
        print(".....................")

        if user_choice == com_choice:
            print("It's a tie!")
            print("...........................")
        elif (user_choice == 1 and com_choice == 2) or \
             (user_choice == 2 and com_choice == 3) or \
             (user_choice == 3 and com_choice == 1):
            print("You won this round!")
            print("...........................")

            user_point += 1
        else:
            print("You lost this round!")
            print("...........................")

            com_point += 1

        print(f"Score: You {user_point} - {com_point} Computer")
        print("------------------------")
    else:
        print("Choose a correct key")
        print("------------------------")

if user_point == 3:
    print("You won overall!")
elif com_point == 3:
    print("You lost overall!")
