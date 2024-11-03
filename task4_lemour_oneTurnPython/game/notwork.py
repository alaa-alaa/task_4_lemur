import random
import tkinter as tk

# Define the game elements and their geometric shapes
elements = {
    "Dagger": {
        "shape": "Triangle",
        "element": "Fire",
        "attack": random.randint(1, 10),  # Random attack value between 1 and 10
        "defense": random.randint(1, 10),  # Random defense value between 1 and 10
    },
    "Iron Cube": {
        "shape": "Pentagon",
        "element": "Earth",
        "attack": random.randint(1, 10),
        "defense": random.randint(1, 10),
    },
    "Wind Carpet": {
        "shape": "Rectangle",
        "element": "Air",
        "attack": random.randint(1, 10),
        "defense": random.randint(1, 10),
    },
    "Dragon": {
        "shape": "Hexagon",
        "element": "Fire",
        "attack": random.randint(1, 10),
        "defense": random.randint(1, 10),
    },
    "Monkey": {
        "shape": "Square",
        "element": "Earth",
        "attack": random.randint(1, 10),
        "defense": random.randint(1, 10),
    },
}


# Define the interaction rules between elements
def get_element_interaction():
    return {
        "Dagger": ["Dragon", "Monkey"],  # Dagger beats Dragon and Monkey
        "Iron Cube": [
            "Dagger",
            "Wind Carpet",
        ],  # Iron Cube beats Dagger and Wind Carpet
        "Wind Carpet": ["Monkey", "Dragon"],  # Wind Carpet beats Monkey and Dragon
        "Dragon": ["Iron Cube", "Monkey"],  # Dragon beats Iron Cube and Monkey
        "Monkey": ["Dagger", "Wind Carpet"],  # Monkey beats Dagger and Wind Carpet
    }


# Determine winner based on element interaction and attack/defense values
def determine_winner(player_choice, computer_choice):
    player_attack = elements[player_choice]["attack"]
    player_defense = elements[player_choice]["defense"]
    computer_attack = elements[computer_choice]["attack"]
    computer_defense = elements[computer_choice]["defense"]

    print(
        f"\n{player_choice} (Attack: {player_attack}, Defense: {player_defense}) vs {computer_choice} (Attack: {computer_attack}, Defense: {computer_defense})"
    )

    interactions = get_element_interaction()

    if computer_choice in interactions[player_choice]:
        return "Player wins based on element interaction!"
    elif player_choice in interactions[computer_choice]:
        return "Computer wins based on element interaction!"
    elif player_attack >= computer_defense:
        return "Player wins based on attack value!"
    elif computer_attack >= player_defense:
        return "Computer wins based on attack value!"
    else:
        return "It's a tie!"


# GUI setup and game display
def play_game(player_choice):
    computer_choice = random.choice(list(elements.keys()))
    result = determine_winner(player_choice, computer_choice)

    # Update GUI
    player_label.config(
        text=f"Player chose: {player_choice} ({elements[player_choice]['shape']})"
    )
    computer_label.config(
        text=f"Computer chose: {computer_choice} ({elements[computer_choice]['shape']})"
    )
    result_label.config(text=result)


# Initialize the main GUI window
root = tk.Tk()
root.title("Elemental Game")

# Create labels and buttons
player_label = tk.Label(root, text="Player chose: ")
player_label.pack()

computer_label = tk.Label(root, text="Computer chose: ")
computer_label.pack()

result_label = tk.Label(root, text="Result: ")
result_label.pack()

# Generate buttons for each element choice
for element in elements:
    button = tk.Button(root, text=element, command=lambda e=element: play_game(e))
    button.pack()

root.mainloop()
