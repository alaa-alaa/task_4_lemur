import random

# تعريف العناصر وقواعد اللعبة
elements = {
    "Dagger": {"beats": ["Magic Carpet", "Monkey"], "shape": "Triangle"},
    "Iron Cube": {"beats": ["Dagger", "Dragon"], "shape": "Cube"},
    "Magic Carpet": {"beats": ["Iron Cube", "Dragon"], "shape": "Rectangle"},
    "Dragon": {"beats": ["Magic Carpet", "Monkey"], "shape": "Hexagon"},
    "Monkey": {"beats": ["Dagger", "Iron Cube"], "shape": "Cylinder"},
}


# دالة لتحديد الفائز
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif computer_choice in elements[player_choice]["beats"]:
        return "You win!"
    else:
        return "Computer wins!"


# تشغيل اللعبة
def play_game():
    print("Welcome to the extended game!")
    print(
        "Choices: Dagger (Triangle), Iron Cube (Cube), Magic Carpet (Rectangle), Dragon (Hexagon), Monkey (Cylinder)"
    )

    # طلب اختيار اللاعب
    player_choice = input(
        "Enter your choice: Dagger, Iron Cube, Magic Carpet, Dragon, or Monkey: "
    ).title()
    if player_choice not in elements:
        print("Invalid choice! Please try again.")
        return

    # اختيار عشوائي للكمبيوتر
    computer_choice = random.choice(list(elements.keys()))

    # طباعة الأشكال الهندسية للاعب والكمبيوتر
    print(f"\nYou chose: {player_choice} - Shape: {elements[player_choice]['shape']}")
    print(
        f"Computer chose: {computer_choice} - Shape: {elements[computer_choice]['shape']}"
    )

    # تحديد وإظهار النتيجة
    result = determine_winner(player_choice, computer_choice)
    print("\nResult:", result)


# استدعاء اللعبة
play_game()
