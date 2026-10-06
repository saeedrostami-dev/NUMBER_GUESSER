import pytest

from main import check_user_input, check_rules, evaluate_performance, game


def test_valid_user_input():
    assert check_user_input("50") == 50


def test_invalid_user_input():
    assert check_user_input("hello") is None


@pytest.mark.parametrize("user_input", ["150", "-1"])
def test_user_input_out_of_range(user_input):
    assert check_user_input(user_input) is None


@pytest.mark.parametrize(
    "user_guess, secret_number, expected",
    [
        (80, 50, False),
        (30, 50, False),
        (50, 50, True),
    ],
)
def test_check_rules(user_guess, secret_number, expected):
    assert check_rules(user_guess, secret_number) is expected


@pytest.mark.parametrize(
    "attempts, expected_out",
    [
        (2, "Excellent! 🎯\n"),
        (5, "Good job! 👍\n"),
        (8, "Not bad! Keep practicing. 💪\n"),
        (12, "You can do better! Keep practicing. 🔥\n"),
    ],
)
def test_evaluate_performance(attempts, expected_out, capsys):
    evaluate_performance(attempts)

    captured = capsys.readouterr()

    assert captured.out == expected_out


@pytest.mark.parametrize(
    "user_input, expected",
    [
        ("0", 0),
        ("100", 100),
        ("", None),
        ("   ", None),
        ("+50", 50),
        ("50.5", None),
        ("0010", 10),
    ],
)
def test_user_input_edge_cases(user_input, expected):
    assert check_user_input(user_input) == expected


def test_game_multiple_guesses(monkeypatch, capsys):
    inputs = iter(["30", "80", "50", "no"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr("main.random.randint", lambda a, b: 50)

    game()

    captured = capsys.readouterr()

    assert "Your guess is lower than the secret number." in captured.out
    assert "Your guess is higher than the secret number." in captured.out
    assert "You won!" in captured.out
    assert "You found the number in 3 attempts!" in captured.out


def test_game_quit(monkeypatch, capsys):
    inputs = iter(["q"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr("main.random.randint", lambda a, b: 50)

    game()

    captured = capsys.readouterr()

    assert "Goodbye!" in captured.out


def test_game_invalid_inputs(monkeypatch, capsys):
    inputs = iter(["hello", "150", "hello", "50", "no"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr("main.random.randint", lambda a, b: 50)

    game()

    captured = capsys.readouterr()

    assert "The guess must be an integer number. Try again!" in captured.out
    assert "The guess must be within the range of 0 to 100." in captured.out
    assert "You won!" in captured.out
    assert "You found the number in 1 attempts!" in captured.out
