# run.py

import os
import sys

def run_hangman():
    os.system(f"{sys.executable} hangman/hangman_game.py")

def run_calculator():
    os.system(f"{sys.executable} calculator/calculator.py")

def run_exit():
    print("👋 Exiting...")
    sys.exit()

def main():
    while True:
        print("\n🎮 Select an option:")
        print("1. Play Hangman")
        print("2. Use Calculator")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            run_hangman()
        elif choice == "2":
            run_calculator()
        elif choice == "3":
            run_exit()
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()


