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
        "shape": "Hexagon",
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
        "shape": "Cylinder",
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


def determine_winner(player_choice, computer_choice):
    player_attack = elements[player_choice]["attack"]
    player_defense = elements[player_choice]["defense"]
    computer_attack = elements[computer_choice]["attack"]
    computer_defense = elements[computer_choice]["defense"]

    print(
        f"\n{player_choice} (Attack: {player_attack}, Defense: {player_defense}) vs {computer_choice} (Attack: {computer_attack}, Defense: {computer_defense})"
    )

    # Determine winner based on interaction and attack/defense values
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


# Main game loop
def play_game():
    print("Welcome to the Dagger, Iron Cube, Wind Carpet, Dragon, and Monkey game!")
    print("Choose your element:")

    for element in elements:
        print(f"- {element} (Shape: {elements[element]['shape']})")

    player_choice = input("Enter your choice: ")
    computer_choice = random.choice(list(elements.keys()))

    if player_choice in elements:
        result = determine_winner(player_choice, computer_choice)
        print(result)
    else:
        print("Invalid choice. Please select a valid element.")


# Start the game
if __name__ == "__main__":
    play_game()
