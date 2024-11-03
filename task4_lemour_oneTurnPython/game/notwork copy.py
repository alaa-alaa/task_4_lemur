import random
import tkinter as tk

# Define the game elements and their geometric shapes
elements = {
    "Dagger": {
        "shape": "Triangle",
        "element": "Fire",
        "attack": random.randint(1, 10),
        "defense": random.randint(1, 10),
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
        "shape": "Square",  # Error: Should be "Cylinder"
        "element": "Earth",
        "attack": random.randint(1, 10),
        "defense": random.randint(1, 10),
    },
}


# Define the interaction rules between elements
def get_element_interaction():
    return {
        "Dagger": ["Dragon", "Monkey"],
        "Iron Cube": ["Dagger", "Wind Carpet"],
        "Wind Carpet": ["Monkey", "Dragon"],
        "Dragon": ["Iron Cube", "Monkey"],
        "Monkey": ["Dagger", "Wind Carpet"],
    }


# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    player_attack = elements[player_choice]["attack"]
    player_defense = elements[player_choice]["defense"]
    computer_attack = elements[computer_choice]["attack"]
    computer_defense = elements[computer_choice]["defense"]

    interactions = get_element_interaction()

    # Logical Condition Error: Incorrect comparison logic
    if (
        computer_choice in interactions[player_choice]
        and player_attack > computer_defense
    ):
        return "Player wins based on element interaction!"
    elif player_choice in interactions[computer_choice]:
        return "Computer wins based on element interaction!"
    elif player_attack >= computer_defense:  # Error: Should be ">"
        return "Player wins based on attack value!"
    elif computer_attack > player_defense:
        return "Computer wins based on attack value!"
    else:
        return "It's a tie!"


# GUI setup
def draw_shape(canvas, shape, x, y):
    if shape == "Triangle":
        canvas.create_polygon(
            x, y, x + 20, y + 40, x - 20, y + 40, fill="red"
        )  # Dagger
    elif shape == "Pentagon":
        canvas.create_polygon(
            x, y, x + 20, y, x + 30, y + 20, x + 10, y + 30, x - 10, y + 20, fill="gray"
        )  # Iron Cube
    elif shape == "Rectangle":
        # Error: Missing drawing logic for Wind Carpet
        pass
    elif shape == "Hexagon":
        canvas.create_polygon(
            x,
            y,
            x + 20,
            y,
            x + 30,
            y + 20,
            x + 20,
            y + 40,
            x,
            y + 40,
            x - 10,
            y + 20,
            fill="blue",
        )  # Dragon
    elif shape == "Square":
        canvas.create_rectangle(x, y, x + 40, y + 40, fill="green")  # Monkey
    else:
        print("Unknown shape!")


def play_game():
    player_choice = "Dagger"  # Example player choice
    computer_choice = "Monkey"  # Example computer choice

    result = determine_winner(player_choice, computer_choice)

    # GUI to show shapes and outcome
    window = tk.Tk()
    window.title("Shape Battle Game")
    canvas = tk.Canvas(window, width=400, height=200)
    canvas.pack()

    # Draw player shape
    draw_shape(canvas, elements[player_choice]["shape"], 50, 50)
    canvas.create_text(50, 120, text=f"Player chose {player_choice}", fill="black")

    # Draw computer shape
    draw_shape(canvas, elements[computer_choice]["shape"], 200, 50)
    canvas.create_text(200, 120, text=f"Computer chose {computer_choice}", fill="black")

    # Display result
    canvas.create_text(200, 180, text=result, fill="purple")

    # Misleading label updates in GUI
    canvas.create_text(
        350, 180, text="Results may vary!", fill="orange"
    )  # Misleading message

    window.mainloop()


# Run the game
if __name__ == "__main__":
    play_game()
