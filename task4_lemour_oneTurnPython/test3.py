import random

# Define the game elements with their properties
elements = {
    "Dagger": {
        "beats": ["Magic Carpet", "Monkey"],
        "shape": "Triangle",
        "element": "Fire",
        "attack": 5,
        "defense": 2,
    },
    "Iron Cube": {
        "beats": ["Dagger", "Dragon"],
        "shape": "Cube",
        "element": "Earth",
        "attack": 3,
        "defense": 6,
    },
    "Magic Carpet": {
        "beats": ["Iron Cube", "Dragon"],
        "shape": "Rectangle",
        "element": "Air",
        "attack": 4,
        "defense": 3,
    },
    "Dragon": {
        "beats": ["Magic Carpet", "Monkey"],
        "shape": "Hexagon",
        "element": "Fire",
        "attack": 6,
        "defense": 4,
    },
    "Monkey": {
        "beats": ["Dagger", "Iron Cube"],
        "shape": "Cylinder",
        "element": "Water",
        "attack": 2,
        "defense": 5,
    },
}


def calculate_result(player, computer):
    """Calculate the result of the game based on player and computer choices."""
    if player == computer:
        return "Tie"
    if computer in elements[player]["beats"]:
        return "Win"
    return "Lose"


def determine_winner(player_choice, computer_choice):
    """Determine the winner and return the result string."""
    result = calculate_result(player_choice, computer_choice)
    if result == "Tie":
        return "It's a tie!"
    elif result == "Win":
        player_attack = elements[player_choice]["attack"]
        computer_defense = elements[computer_choice]["defense"]
        if player_attack > computer_defense:
            return f"You win with a powerful attack using {player_choice}!"
        else:
            return f"You barely win using {player_choice}!"
    else:
        computer_attack = elements[computer_choice]["attack"]
        player_defense = elements[player_choice]["defense"]
        if computer_attack > player_defense:
            return f"Computer wins with a powerful attack using {computer_choice}!"
        else:
            return f"Computer wins, but barely with {computer_choice}!"


def play_game():
    """Main game loop."""
    print("Welcome to the Extended Rock-Paper-Scissors Game!")
    print("Available choices:")
    for element in elements.keys():
        print(
            f"- {element} (Shape: {elements[element]['shape']}, Element: {elements[element]['element']})"
        )

    while True:
        player_choice = input(
            "\nChoose your element (or type 'exit' to quit): "
        ).capitalize()
        if player_choice == "Exit":
            print("Thanks for playing!")
            break

        if player_choice not in elements:
            print("Invalid choice, please try again.")
            continue

        computer_choice = random.choice(list(elements.keys()))
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)


if __name__ == "__main__":
    play_game()
