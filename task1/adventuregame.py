import random

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_item(self, item):
        print(f"You found a {item}!")
        self.inventory.append(item)

    def has_item(self, item):
        return item in self.inventory

def start_game():
    print("Welcome to the Forest Adventure!")
    name = input("Enter your name: ")
    player = Player(name)
    print(f"\nHello, {player.name}! You find yourself at a fork in the forest path.")

    while True:
        choice = input("\nDo you want to go left or right? (left/right): ").lower()
        if choice == "left":
            left_path(player)
            break
        elif choice == "right":
            right_path(player)
            break
        else:
            print("Invalid choice. Please type 'left' or 'right'.")

def left_path(player):
    print("\nYou walk left and discover a hidden treasure chest!")
    item = random.choice(["mysterious key", "ancient coin", "healing potion"])
    player.add_item(item)
    next_choice(player)

def right_path(player):
    print("\nYou walk right and encounter a wild animal!")
    if player.has_item("mysterious key"):
        print("You use the mysterious key to distract the animal and escape safely.")
    else:
        print("You have nothing to defend yourself. The animal attacks you. Game over.")
        return
    next_choice(player)

def next_choice(player):
    while True:
        choice = input("\nDo you want to continue exploring or head back? (explore/back): ").lower()
        if choice == "explore":
            print("\nYou venture deeper into the forest and find a peaceful clearing. You rest here. The adventure continues...")
            break
        elif choice == "back":
            print("\nYou decide to head back to safety. Adventure ends here.")
            break
        else:
            print("Invalid choice. Please type 'explore' or 'back'.")

if __name__ == "__main__":
    start_game()
