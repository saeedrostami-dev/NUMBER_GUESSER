# 🎯 Number Guesser

A simple command-line number guessing game built with Python.

The computer randomly selects a number between **0 and 100**, and the player tries to guess it. After each valid guess, the game provides a hint indicating whether the guess is higher or lower than the secret number.

The project also includes automated tests using **pytest**.

## ✨ Features

* 🎲 Random secret number between `0` and `100`
* 🔢 Validation of user input
* 🚫 Handling invalid and out-of-range inputs
* 💡 Higher/lower hints after each guess
* 📊 Performance evaluation based on the number of attempts
* 🔁 Option to play multiple games
* 🚪 Ability to quit the game with `q`
* 🧪 Automated tests with `pytest`
* 🧩 Integration tests using `monkeypatch`
* 📦 Python code organized into reusable functions

## 🛠️ Technologies

* Python 3
* pytest
* Git

## 📁 Project Structure

```text
NUMBER_GUESSER/
│
├── main.py          # Main game logic
├── test_game.py     # Automated tests
├── .gitignore       # Ignored files and directories
└── README.md        # Project documentation
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd NUMBER_GUESSER
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Linux/macOS:

```bash
source .venv/bin/activate
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

Install pytest:

```bash
pip install pytest
```

## ▶️ Run the Game

Run the following command:

```bash
python main.py
```

You will be asked to enter a number between `0` and `100`.

Example:

```text
Please enter your number guess between 0 and 100, or press 'q' to exit: 30
Attempt #1
That is your guess: 30.

Your guess is lower than the secret number.

Please enter your number guess between 0 and 100, or press 'q' to exit: 70
Attempt #2
That is your guess: 70.

Your guess is higher than the secret number.

Please enter your number guess between 0 and 100, or press 'q' to exit: 50
Attempt #3
That is your guess: 50.

You won!
You found the number in 3 attempts!
Excellent! 🎯
```

## 🧪 Run Tests

Run the complete test suite with:

```bash
pytest
```

Or:

```bash
python -m pytest
```

The test suite covers:

* Valid user input
* Invalid input
* Out-of-range values
* Boundary values
* Higher/lower/equal guesses
* Performance evaluation
* Multiple guesses during a game
* Invalid inputs during gameplay
* Quitting the game

## 🧠 What I Practiced

This project was built as a practical Python learning project and focuses on several important concepts:

* Functions
* Type hints
* Exception handling with `try/except`
* Loops
* Conditional statements
* User input
* Random number generation
* Function decomposition
* Automated testing with pytest
* `pytest.mark.parametrize`
* `capsys`
* `monkeypatch`
* Basic Git workflow
* Project documentation

## 📌 Future Improvements

Possible improvements for future versions:

* Add difficulty levels
* Add a maximum number of attempts
* Add a score system
* Store high scores
* Add a graphical interface
* Improve the game architecture as the project grows

## 👤 Author

**Saeed**

This project is part of my journey to improve my Python programming and software development skills.
