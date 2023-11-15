import sys
import time
import random

def start_game():
    print("Welcome to the Maze Escape Game!")
    input("Press Enter to begin...")
    print("You find yourself trapped in a mysterious maze. Your goal is to reach the exit.")

    # Replace this section with your maze generation and gameplay logic
    # For simplicity, I'll just simulate the player reaching the exit
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