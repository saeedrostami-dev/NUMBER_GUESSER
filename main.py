import random


def check_user_input(user_input: str) -> int | None:
    """Validate the user's input and return it as an integer."""

    if not user_input:
        print("The guess shouldn't be left blank.")
        return None

    try:
        user_guess = int(user_input)
    except ValueError:
        print("The guess must be an integer number. Try again!")
        return None

    if not 0 <= user_guess <= 100:
        print("The guess must be within the range of 0 to 100.")
        return None

    return user_guess


def check_rules(user_guess: int, secret_number: int) -> bool:
    """Compare the user's guess with the secret number and display the result."""

    if user_guess > secret_number:
        print("Your guess is higher than the secret number.\n")
        return False

    if user_guess < secret_number:
        print("Your guess is lower than the secret number.\n")
        return False

    print("You won!")
    return True


def evaluate_performance(attempts: int) -> None:
    """Evaluate and display the player's performance based on attempts."""

    if attempts <= 3:
        print("Excellent! 🎯")
    elif attempts <= 6:
        print("Good job! 👍")
    elif attempts <= 10:
        print("Not bad! Keep practicing. 💪")
    else:
        print("You can do better! Keep practicing. 🔥")


def play_again() -> bool:
    while True:
        answer = input("Do you want to play again? (yes/no): ").strip().lower()

        if answer == "yes":
            print("-- Next game --")
            return True

        if answer == "no":
            print("Okay, thank you for playing. Goodbye!")
            return False

        print("Please enter yes or no.")


def game() -> None:
    while True:
        secret_number = random.randint(0, 100)
        attempts = 0

        while True:
            user_input = input(
                "Please enter your number guess between 0 and 100, "
                "or press 'q' to exit: "
            ).strip().lower()

            if user_input == "q":
                print("Goodbye!")
                return

            user_guess = check_user_input(user_input)

            if user_guess is None:
                continue

            attempts += 1

            print(f"Attempt #{attempts}")
            print(f"That is your guess: {user_guess}.\n")

            if check_rules(user_guess, secret_number):
                print(f"You found the number in {attempts} attempts!")
                evaluate_performance(attempts)
                print()
                break

        if not play_again():
            break


if __name__ == "__main__":
    game()
