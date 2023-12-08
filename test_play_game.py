from play_game import PlayGame

def test_difficulty_input_validity():
    difficulty = 4
    difficulty = test_test_difficulty_input_validity(difficulty)
    print(difficulty)


def test_test_difficulty_input_validity(difficulty):
    while difficulty not in range(0, 3):
        difficulty = int(input("invalid input, please enter number between 1 to 3:"))

    return difficulty

def main():
    test_difficulty_input_validity()

main()