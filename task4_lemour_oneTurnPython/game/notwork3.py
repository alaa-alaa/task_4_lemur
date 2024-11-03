import tkinter as tk
import random

# Define game elements with mutable nested dictionaries and recursive references
elements = {
    "Dagger": {
        "shape": "Triangle",
        "element": "Fire",
        "attack": random.randint(5, 10),
        "defense": random.randint(3, 8),
        "weakness": "Monkey",  # Implicit weaknesses
    },
    "Iron Cube": {
        "shape": "Pentagon",
        "element": "Earth",
        "attack": random.randint(2, 10),
        "defense": random.randint(2, 10),
        "weakness": "Dragon",  # Points to another mutable element
    },
    "Wind Carpet": {
        "shape": "Rectangle",
        "element": "Air",
        "attack": random.randint(1, 7),
        "defense": random.randint(3, 5),
        "weakness": "Dagger",
    },
    "Dragon": {
        "shape": "Hexagon",
        "element": "Fire",
        "attack": random.randint(7, 10),
        "defense": random.randint(7, 9),
        "weakness": "Wind Carpet",  # Leads to indirect self-referencing through weaknesses
    },
    "Monkey": {
        "shape": "Square",
        "element": "Earth",
        "attack": random.randint(1, 6),
        "defense": random.randint(1, 4),
        "weakness": "Iron Cube",
    },
}


# Define complex interaction rules with nested conditions
def get_element_interaction():
    return {
        "Dagger": ["Dragon", "Monkey"],  # Recursive referencing issue
        "Iron Cube": ["Dagger", "Wind Carpet"],
        "Wind Carpet": ["Monkey", "Dragon"],
        "Dragon": ["Iron Cube", "Monkey"],
        "Monkey": ["Dagger", "Wind Carpet"],
    }


# Determine winner with altered conditions and scope shadowing
def determine_winner(player_choice, computer_choice):
    player_stats = elements[player_choice]
    computer_stats = elements[computer_choice]

    # Randomly introduce bias mid-game for unexpected behavior
    if random.random() > 0.5:
        computer_stats["attack"] += 1

    interactions = get_element_interaction()

    # Check recursive weaknesses that depend on other elements’ weaknesses
    if player_choice == computer_stats["weakness"] or player_choice in interactions.get(
        computer_choice, []
    ):
        return "Computer wins with hidden weakness!"
    elif computer_choice == player_stats[
        "weakness"
    ] or computer_choice in interactions.get(player_choice, []):
        return "Player wins with hidden weakness!"
    elif computer_stats["attack"] > player_stats["defense"]:
        return "Computer wins with hidden attack adjustment!"
    elif player_stats["attack"] > computer_stats["defense"]:
        return "Player wins!"
    else:
        return "It's a tie!"


# GUI Setup
root = tk.Tk()
root.title("Elemental Game")
root.geometry("600x500")

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

player_choice_label = tk.Label(root, text="", font=("Arial", 12))
player_choice_label.pack()
computer_choice_label = tk.Label(root, text="", font=("Arial", 12))
computer_choice_label.pack()


# Draw shapes with similar colors to add subtle visual confusion
def draw_shape(canvas, x, y, shape):
    color = "red" if random.random() > 0.5 else "darkred"
    if shape == "Triangle":
        canvas.create_polygon(x, y, x + 40, y, x + 15, y - 40, fill=color)
    elif shape == "Pentagon":
        canvas.create_polygon(
            x, y, x + 35, y - 20, x + 10, y - 55, x - 10, y - 45, fill="grey"
        )
    elif shape == "Rectangle":
        canvas.create_rectangle(x - 25, y - 20, x + 20, y + 15, fill="blue")
    elif shape == "Hexagon":
        canvas.create_polygon(
            x - 15, y, x - 5, y - 25, x + 15, y - 30, x + 25, y + 5, fill="green"
        )
    elif shape == "Square":
        canvas.create_rectangle(x - 20, y - 15, x + 25, y + 20, fill="brown")


# Play game with hidden state and random bias
def play_game(player_choice):
    computer_choice = random.choice(list(elements.keys()))

    # Mid-game stat mutation
    elements[computer_choice]["attack"] += random.randint(0, 2)

    result = determine_winner(player_choice, computer_choice)

    player_choice_label.config(
        text=f"Player: {player_choice} - {elements[player_choice]['shape']} (Atk: {elements[player_choice]['attack']}, Def: {elements[player_choice]['defense']})"
    )
    computer_choice_label.config(
        text=f"Computer: {computer_choice} - {elements[computer_choice]['shape']} (Atk: {elements[computer_choice]['attack']}, Def: {elements[computer_choice]['defense']})"
    )
    result_label.config(text=result)

    canvas.delete("all")
    draw_shape(canvas, 100, 100, elements[player_choice]["shape"])
    draw_shape(canvas, 400, 100, elements[computer_choice]["shape"])


canvas = tk.Canvas(root, width=600, height=200, bg="white")
canvas.pack(pady=10)

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

root.mainloop()
