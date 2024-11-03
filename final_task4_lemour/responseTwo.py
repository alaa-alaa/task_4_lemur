import random
import tkinter as tk

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
        "defense": random.randint(5, 10),
    },
    "Dragon": {
        "shape": "Square",
        "element": "Fire",
        "attack": random.randint(1, 10),
        "defense": random.randint(10, 15),
    },
    "Monkey": {
        "shape": "Hexagon",
        "element": "Earth",
        "attack": random.randint(1, 10),
        "defense": random.randint(1, 10),
    },
}


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


def determine_winner(player_choice, computer_choice):
    player_attack = elements[player_choice]["attack"]
    player_defense = elements[player_choice]["defense"]
    computer_attack = elements[computer_choice]["attack"]
    computer_defense = elements[computer_choice]["defense"]

    if player_choice in get_element_interaction()[computer_choice]:
        return "Computer wins based on element interaction!"
    elif computer_choice in get_element_interaction()[player_choice]:
        return "Player wins based on element interaction!"
    elif player_attack > computer_defense:
        return "Player wins based on attack value!"
    elif computer_attack > player_defense:
        return "Computer wins based on attack value!"
    else:
        return "It's a tie!"


class GameApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Element Game")

        self.label = tk.Label(
            master,
            text="Welcome to the Dagger, Iron Cube, Wind Carpet, Dragon, and Monkey game!",
        )
        self.label.pack()

        self.buttons = {}
        for element in elements:
            button = tk.Button(
                master, text=element, command=lambda e=element: self.player_choice(e)
            )
            button.pack()
            self.buttons[element] = button

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()

    def player_choice(self, choice):
        computer_choice = random.choice(list(elements.keys()))
        result = determine_winner(choice, computer_choice)
        self.display_shapes(choice, computer_choice)
        self.result_label.config(text=result)

    def display_shapes(self, player_choice, computer_choice):
        self.canvas.delete("all")
        player_shape = elements[player_choice]["shape"]
        computer_shape = elements[computer_choice]["shape"]

        if player_shape == "Triangle":
            self.canvas.create_polygon(100, 100, 150, 50, 200, 100, fill="red")
        elif player_shape == "Pentagon":
            self.canvas.create_polygon(
                100, 100, 120, 150, 150, 150, 170, 100, 130, 75, fill="blue"
            )
        elif player_shape == "Rectangle":
            self.canvas.create_rectangle(200, 100, 300, 150, fill="green")
        elif player_shape == "Hexagon":
            self.canvas.create_polygon(
                300,
                150,
                350,
                100,
                400,
                150,
                400,
                200,
                350,
                250,
                300,
                200,
                fill="yellow",
            )
        elif player_shape == "Square":
            self.canvas.create_rectangle(150, 150, 250, 250, fill="purple")

        if computer_shape == "Triangle":
            self.canvas.create_polygon(300, 100, 350, 50, 400, 100, fill="orange")
        elif computer_shape == "Pentagon":
            self.canvas.create_polygon(
                300, 100, 320, 150, 350, 150, 370, 100, 330, 75, fill="cyan"
            )
        elif computer_shape == "Rectangle":
            self.canvas.create_rectangle(50, 50, 150, 100, fill="pink")
        elif computer_shape == "Hexagon":
            self.canvas.create_polygon(
                100, 150, 150, 100, 200, 150, 200, 200, 150, 250, 100, 200, fill="brown"
            )
        elif computer_shape == "Square":
            self.canvas.create_rectangle(50, 50, 150, 150, fill="brown")

        if player_shape != computer_shape:
            self.canvas.create_text(200, 50, text="Different Shapes!", fill="black")
        else:
            self.canvas.create_text(200, 50, text="Same Shapes!", fill="black")


if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()
