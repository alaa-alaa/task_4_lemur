import tkinter as tk
import random

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


# Determine the winner
def determine_winner(player_choice, computer_choice):
    player_attack = elements[player_choice]["attack"]
    player_defense = elements[player_choice]["defense"]
    computer_attack = elements[computer_choice]["attack"]
    computer_defense = elements[computer_choice]["defense"]

    interactions = get_element_interaction()
    if computer_choice in interactions[player_choice]:
        return "Player wins based on element interaction!"
    elif player_choice in interactions[computer_choice]:
        return "Computer wins based on element interaction!"
    elif player_attack > computer_defense:
        return "Player wins based on attack value!"
    elif computer_attack > player_defense:
        return "Computer wins based on attack value!"
    else:
        return "It's a tie!"


# GUI Setup
root = tk.Tk()
root.title("Elemental Game")
root.geometry("600x500")

# Display game results
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Display chosen elements with attack and defense values
player_choice_label = tk.Label(root, text="", font=("Arial", 12))
player_choice_label.pack()
computer_choice_label = tk.Label(root, text="", font=("Arial", 12))
computer_choice_label.pack()


# Draw shapes based on the selected element
def draw_shape(canvas, x, y, shape):
    if shape == "Triangle":
        canvas.create_polygon(x, y, x + 40, y, x + 20, y - 35, fill="red")
    elif shape == "Pentagon":
        canvas.create_polygon(
            x,
            y,
            x + 30,
            y - 20,
            x + 15,
            y - 50,
            x - 15,
            y - 50,
            x - 30,
            y - 20,
            fill="grey",
        )
    elif shape == "Rectangle":
        canvas.create_rectangle(x - 20, y - 20, x + 20, y + 20, fill="blue")
    elif shape == "Hexagon":
        canvas.create_polygon(
            x - 20,
            y,
            x - 10,
            y - 30,
            x + 10,
            y - 30,
            x + 20,
            y,
            x + 10,
            y + 30,
            x - 10,
            y + 30,
            fill="green",
        )
    elif shape == "Square":
        canvas.create_rectangle(x - 20, y - 20, x + 20, y + 20, fill="brown")


# Play the game and update the GUI
def play_game(player_choice):
    computer_choice = random.choice(list(elements.keys()))

    # Determine the winner
    result = determine_winner(player_choice, computer_choice)

    # Update labels with player and computer choices and attributes
    player_choice_label.config(
        text=f"Player chose {player_choice} - {elements[player_choice]['shape']} (Attack: {elements[player_choice]['attack']}, Defense: {elements[player_choice]['defense']})"
    )
    computer_choice_label.config(
        text=f"Computer chose {computer_choice} - {elements[computer_choice]['shape']} (Attack: {elements[computer_choice]['attack']}, Defense: {elements[computer_choice]['defense']})"
    )
    result_label.config(text=result)

    # Update canvas with shapes
    canvas.delete("all")
    draw_shape(canvas, 100, 100, elements[player_choice]["shape"])
    draw_shape(canvas, 400, 100, elements[computer_choice]["shape"])


# Create a canvas for shapes
canvas = tk.Canvas(root, width=600, height=200, bg="white")
canvas.pack(pady=10)

# Buttons for each element
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

for element in elements.keys():
    button = tk.Button(
        button_frame,
        text=element,
        command=lambda e=element: play_game(e),
        width=15,
        height=2,
    )
    button.pack(side="left", padx=5)

# Run the main loop
root.mainloop()
