import random

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
=========''', r'''
  +---+
  |   |
 [O   |
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

def load_words(filename):
    with open(filename, "r", encoding="utf-8") as f:
        words = [line.strip() for line in f if line.strip()]
    return words

def choose_word(words):
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    words = load_words("words.txt")
    word = choose_word(words)
    guessed_letters = set()
    tries = 0
    max_tries = 10 

    print("Sveiki atvykę į Hangman žaidimą!")
    print(f"Atspėkite žodį. Jūs turite {max_tries} bandymų.\n")

    while tries < max_tries:
        print(HANGMANPICS[tries])
        print(display_word(word, guessed_letters))
        guess = input("Spėkite raidę arba visą žodį: ").strip().lower()

        if len(guess) == 1:
            if guess in guessed_letters:
                print("Šią raidę jau spėjote.")
            elif guess in word:
                guessed_letters.add(guess)
                print("Teisingai!")
            else:
                guessed_letters.add(guess)
                tries += 1
                print(f"Neteisinga raidė! Bandymų liko: {max_tries - tries}")
        else:
            if guess == word:
                print(f"Puiku! Teisingai atspėjote žodį: {word}")
                return
            else:
                tries += 1
                print(f"Neteisingas žodis! Bandymų liko: {max_tries - tries}")

        if all(letter in guessed_letters for letter in word):
            print(f"Puiku! Jūs atspėjote žodį: {word}")
            return

        print()

    print(HANGMANPICS[-1])
    print(f"GAME OVER. Žodis buvo: {word}")

if __name__ == "__main__":
    hangman()
