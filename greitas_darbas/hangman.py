import random
import re
from typing import List, Set, Optional

HANGMANPICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
 /|\  |
 / \  |
      |
=========''', r'''
  +---+
  |   |
 [O]  |
 /|\  |
 / \  |
      |
=========''', r'''
  +---+
  |   |
 [O]  |
[/|\  |
 / \  |
      |
=========''', r'''
  +---+
  |   |
 [O]  |
[/|\] |
 / \  |
      |
=========''']

VALID_LETTER_PATTERN = re.compile(r"^[a-ząčęėįšųūž]+$")

def load_words(filename: str) -> List[str]:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return [line.strip().lower() for line in f if line.strip()]
    except FileNotFoundError:
        print("Error: 'words.txt' file not found.")
        return []

def choose_word(words: List[str], used_words: Set[str]) -> Optional[str]:
    available = [w for w in words if w not in used_words]
    if not available:
        return None
    return random.choice(available)

def display_word(word: str, guessed_letters: Set[str]) -> str:
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def is_valid_input(text: str) -> bool:
    return bool(VALID_LETTER_PATTERN.fullmatch(text))

def hangman() -> None:
    words = load_words("words.txt")
    if not words:
        print("The game requires a 'words.txt' file with at least one word.")
        return

    used_words: Set[str] = set()
    play_again: bool = True

    while play_again:
        word = choose_word(words, used_words)
        if not word:
            print("No more new words available. Game over!")
            break
        used_words.add(word)

        guessed_letters: Set[str] = set()
        tries: int = 0
        max_tries: int = 10

        print("\n--- New round! ---")
        print(f"Guess the word. You have {max_tries} tries.\n")

        while tries < max_tries:
            print(HANGMANPICS[tries])
            print(display_word(word, guessed_letters))
            if guessed_letters:
                print("Guessed letters: " + ", ".join(sorted(guessed_letters)))

            guess: str = input("Guess a letter or the whole word: ").strip().lower()

            if not guess:
                print("Please enter at least one letter.")
                continue

            if not is_valid_input(guess):
                print("Only Lithuanian lowercase letters are allowed, no numbers or symbols!")
                continue

            if len(guess) == 1:
                if guess in guessed_letters:
                    print("You already guessed that letter.")
                    continue
                if guess in word:
                    guessed_letters.add(guess)
                    print("Correct!")
                else:
                    guessed_letters.add(guess)
                    tries += 1
                    print(f"Wrong letter! Tries left: {max_tries - tries}")
            else:
                if guess == word:
                    print(f"Great! You guessed the word: {word}")
                    break
                else:
                    tries += 2
                    print(f"Wrong word! Tries left: {max_tries - tries}")

            if all(letter in guessed_letters for letter in word):
                print(f"Well done! You guessed the word: {word}")
                break

            print()

        else:
            print(HANGMANPICS[-1])
            print(f"GAME OVER. The word was: {word}")

        choice: str = input("Do you want to play again? (yes/no): ").strip().lower()
        play_again = choice == "yes"

if __name__ == "__main__":
    hangman()