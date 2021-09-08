import random

n = 1
i = 0
e = 0
options = ["R", "P", "S"]

print("Welcome")

while True:
    while n <= 5:
        n = n + 1
        player_option = input(f"Select one of these: {options}\n>")
        computer_option = random.choice(options)
        if player_option == computer_option:
            print(f"You take {player_option}, I take {computer_option}")
            print("it's a tie")
        elif player_option == 'R' and computer_option == 'P':
            e = e  + 1
            print(f"You take {player_option}, I take {computer_option}")
            print(f"You Lose! Your score: {i}, my score: {e}")
        elif player_option == 'R' and computer_option == 'S':
            i = i + 1
            print(f"You take {player_option}, I take {computer_option}")
            print(f"You win! Your score: {i}, my score: {e}")
        elif player_option == 'P' and computer_option == 'S':
            e = e + 1
            print(f"You take {player_option}, I take {computer_option}")
            print(f"You lose! Your score: {i}, my score: {e}")
        elif player_option == 'P' and computer_option == 'R':
            i = i + 1
            print(f"You take {player_option}, I take {computer_option}")
            print(f"You win! Your score: {i}, my score: {e}")
        elif player_option == 'S' and computer_option == 'R':
            e = e + 1
            print(f"You take {player_option}, I take {computer_option}")
            print(f"You lose! Your score: {i}, my score: {e}")
        elif player_option == 'S' and computer_option == 'P':
            i = i + 1
            print(f"You take {player_option}, I take {computer_option}")
            print(f"You win! Your score: {i}, my score: {e}")
        else:
            print(f"Hmmm.... Seems like you wanted to choose one from these: {options}(Please use capital letters only)")
            n = n - 1
    if n > 5:
        if e > i:
            print(f"You Lose the Match!\nYour Points: {i}\nMy Points: {e}")
            n = 1
            i = 0
            e = 0
        elif e < i:
            print(f"You Win the Match!\nYour Points: {i}\nMy Points: {e}")
            n = 1
            i = 0
            e = 0
        else:
            print(f"The match results in a draw!\nYour Points: {i}\nMy Points: {e}")
            n = 1
            i = 0
            e = 0
        hmm = input("Do you wan to continue Y/N\n>")
        if hmm == 'Y':
            continue
        elif hmm == 'N':
          exit()
        else:
            print("Seems like you wanted to write something else. We are restarting the game")
            continue