import sys
import time
import random

def start_game():
    print("""""With your passion for the legend of the keyboard, you venture to the desert to acquire the lost remaining symbol relics that will complete the keyboard. The symbols !,$,&,* and ~.

Your companion, Jebrael, helped you to get to the location because only you 1 were the last person in your bloodline who has the capabilities to take hold of them and place them to the right location.

On the last leg, you finally acquire the “~” symbol. However the whole place started shaking.
""""")
    player_name = input("Enter your username: ")
    input("Press Enter to begin...")
    print(f"{player_name}, you find yourself trapped in a mysterious maze. Your goal is to reach the exit.")

    simulate_maze_escape()

def credits():
    print("Game created by Your Name")

def simulate_maze_escape():
    print("Simulating maze escape...")
    time.sleep(2)
    print("Congratulations! You have escaped the maze.")
    sys.exit()

while True:
    print("\n1. Start Game")
    print("2. Credits")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        start_game()
    elif choice == "2":
        credits()
    elif choice == "3":
        print("Thanks for playing. Goodbye!")
        sys.exit()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
