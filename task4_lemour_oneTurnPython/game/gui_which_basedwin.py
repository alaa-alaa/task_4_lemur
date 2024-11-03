import random
import tkinter as tk
from tkinter import messagebox

# Define the game elements and their geometric shapes
elements = {
    "Dagger": {
        "shape": "Triangle",
        "element": "Fire",
        "attack": random.randint(1, 10),  # Random attack value between 1 and 10
        "defense": random.randint(1, 10),  # Random defense value between 1 and 10
    },
    "Iron Cube": {
        "shape": "Pentagon",  # Shape set to Pentagon
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
        "shape": "Square",  # Updated shape to Square
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


# Determine the winner based on player and computer choices
def determine_winner(player_choice, computer_choice):
    player_attack = elements[player_choice]["attack"]
    player_defense = elements[player_choice]["defense"]
    computer_attack = elements[computer_choice]["attack"]
    computer_defense = elements[computer_choice]["defense"]

    # Determine winner based on interaction and attack/defense values
    interactions = get_element_interaction()

    if computer_choice in interactions[player_choice]:
        return (
            "Player wins based on element interaction!",
            player_choice,
            computer_choice,
            player_attack,
            player_defense,
            computer_attack,
            computer_defense,
        )
    elif player_choice in interactions[computer_choice]:
        return (
            "Computer wins based on element interaction!",
            player_choice,
            computer_choice,
            player_attack,
            player_defense,
            computer_attack,
            computer_defense,
        )
    elif player_attack > computer_defense:
        return (
            "Player wins based on attack value!",
            player_choice,
            computer_choice,
            player_attack,
            player_defense,
            computer_attack,
            computer_defense,
        )
    elif computer_attack > player_defense:
        return (
            "Computer wins based on attack value!",
            player_choice,
            computer_choice,
            player_attack,
            player_defense,
            computer_attack,
            computer_defense,
        )
    else:
        return (
            "It's a tie!",
            player_choice,
            computer_choice,
            player_attack,
            player_defense,
            computer_attack,
            computer_defense,
        )


# Function to draw shapes on the canvas
def draw_shape(canvas, shape, x, y, size, label, attack, defense):
    if shape == "Triangle":
        canvas.create_polygon(x, y, x + size, y, x + size / 2, y - size, fill="red")
    elif shape == "Pentagon":
        pentagon = [
            x,
            y - size,
            x + size * 0.951,
            y - size / 3,
            x + size * 0.588,
            y + size * 0.809,
            x - size * 0.588,
            y + size * 0.809,
            x - size * 0.951,
            y - size / 3,
        ]
        canvas.create_polygon(pentagon, fill="purple")
    elif shape == "Hexagon":
        hexagon = [
            x,
            y - size,
            x + size * 0.866,
            y - size / 2,
            x + size * 0.866,
            y + size / 2,
            x,
            y + size,
            x - size * 0.866,
            y + size / 2,
            x - size * 0.866,
            y - size / 2,
        ]
        canvas.create_polygon(hexagon, fill="green")
    elif shape == "Rectangle":
        canvas.create_rectangle(
            x - size / 2, y - size / 4, x + size / 2, y + size / 4, fill="blue"
        )
    elif shape == "Square":  # Drawing the square shape
        canvas.create_rectangle(
            x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill="orange"
        )

    # Draw the label above the shape
    canvas.create_text(x, y - size - 10, text=label, fill="black", font=("Arial", 10))
    # Draw the attack and defense values below the shape
    canvas.create_text(
        x,
        y + size + 10,
        text=f"Attack: {attack}\nDefense: {defense}",
        fill="black",
        font=("Arial", 10),
    )


# GUI setup
def play_game_gui():
    root = tk.Tk()
    root.title("Dagger, Iron Cube, Wind Carpet, Dragon, Monkey Game")

    # Create a canvas for drawing shapes
    canvas = tk.Canvas(root, width=600, height=400, bg="white")
    canvas.pack()

    # Dropdown for player choice
    player_choice_var = tk.StringVar(root)
    player_choice_var.set(list(elements.keys())[0])  # Default value
    player_choice_menu = tk.OptionMenu(root, player_choice_var, *elements.keys())
    player_choice_menu.pack()

    # Label to display the winner
    winner_label = tk.Label(root, text="", font=("Arial", 14))
    winner_label.pack()

    def start_game():
        player_choice = player_choice_var.get()
        computer_choice = random.choice(list(elements.keys()))

        # Determine the winner
        (
            result,
            player_shape,
            computer_shape,
            player_attack,
            player_defense,
            computer_attack,
            computer_defense,
        ) = determine_winner(player_choice, computer_choice)

        # Show a message box with the result and choices
        messagebox.showinfo(
            "Game Result",
            f"{result}\n\nPlayer chose: {player_shape}\nComputer chose: {computer_shape}",
        )

        # Clear the canvas and draw shapes
        canvas.delete("all")
        draw_shape(
            canvas,
            elements[player_choice]["shape"],
            100,
            300,
            50,
            "Player",
            player_attack,
            player_defense,
        )  # Draw player shape with values
        draw_shape(
            canvas,
            elements[computer_choice]["shape"],
            400,
            300,
            50,
            "Computer",
            computer_attack,
            computer_defense,
        )  # Draw computer shape with values

        # Display choices on the canvas
        canvas.create_text(
            100,
            250,
            text=f"Player chose: {player_choice}",
            fill="black",
            font=("Arial", 10),
        )
        canvas.create_text(
            400,
            250,
            text=f"Computer chose: {computer_choice}",
            fill="black",
            font=("Arial", 10),
        )

        # Display the reason for winning on the label
        winner_label.config(text=f"Winner: {result.split()[0]} ({result})")

    # Start button
    start_button = tk.Button(root, text="Start Game", command=start_game)
    start_button.pack()

    root.mainloop()


# Start the GUI game
if __name__ == "__main__":
    play_game_gui()
