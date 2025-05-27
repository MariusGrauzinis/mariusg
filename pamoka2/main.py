# Create a CLI application that would let user enter random lentgh text.(minimum 5 sentences)
# This random text then should be cleaned: All words which start after end of sentence should start with capital letter, there should be a gap after comma.The Option 1: GET Report option should give answer in this format:

# {
#     "fixed_text": 'text',
#     "number_of_words": 'number_of_words',
#     "number_of_sentences": 'number_of_sentences'
#     "count_of_numbers": 'count_of_numbers' //how many numbers were in the text
#     "most common word/words": 'most common word'
# }

# There should be other options as well for every other field.

# Code must include:
#  - Class (if applicable: All 4 OOP principles, static, class methods, property decorators, dataclasses, use at least 3 python magic methods)
#  - Types everywhere
#  - Logging setup
#  - Error handling 
#  - Github Repo



import re
from collections import Counter
from dataclasses import dataclass
from typing import List
import logging

# Setup logger
logger = logging.getLogger("TextProcessor")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

@dataclass
class TextReport:
    fixed_text: str
    number_of_words: int
    number_of_sentences: int
    count_of_numbers: int
    most_common_words: str

    def __str__(self) -> str:
        return str(self.__dict__)

    def __repr__(self) -> str:
        return f"<TextReport with {self.number_of_words} words>"

class TextProcessor:
    def __init__(self, raw_text: str) -> None:
        self.raw_text = raw_text
        logger.debug("TextProcessor initialized")

    def __len__(self) -> int:
        return len(self.words)

    def __str__(self) -> str:
        return self.fixed_text

    def __repr__(self) -> str:
        return f"<TextProcessor text_length={len(self.raw_text)}>"

    @staticmethod
    def clean_text(text: str) -> str:
        logger.info("Cleaning text")
        text = re.sub(r',(\S)', r', \1', text)
        sentences = re.split(r'(?<=[.!?]) +', text.strip())
        cleaned = ' '.join(s[0].upper() + s[1:] if s else '' for s in sentences)
        return cleaned

    @property
    def fixed_text(self) -> str:
        return self.clean_text(self.raw_text)

    @property
    def words(self) -> List[str]:
        return re.findall(r'\b\w+\b', self.fixed_text)

    @property
    def number_of_words(self) -> int:
        return len(self.words)

    @property
    def number_of_sentences(self) -> int:
        return len(re.findall(r'[.!?]', self.fixed_text))

    @property
    def count_of_numbers(self) -> int:
        return len([word for word in self.words if word.isdigit()])

    @property
    def most_common_words(self) -> str:
        counts = Counter(word.lower() for word in self.words if not word.isdigit())
        max_freq = max(counts.values(), default=0)
        most_common = [w for w, c in counts.items() if c == max_freq]
        return ', '.join(most_common)

    def generate_report(self) -> TextReport:
        return TextReport(
            fixed_text=self.fixed_text,
            number_of_words=self.number_of_words,
            number_of_sentences=self.number_of_sentences,
            count_of_numbers=self.count_of_numbers,
            most_common_words=self.most_common_words
        )

def get_user_text() -> str:
    print("Enter your text (at least one sentence). Press Enter twice to finish:")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return ' '.join(lines)

def main() -> None:
    try:
        raw_text = get_user_text()
        if not raw_text.strip():
            print("You must enter some text.")
            return

        processor = TextProcessor(raw_text)

        while True:
            print("\nOptions:")
            print("1. GET Full Report")
            print("2. Show Fixed Text")
            print("3. Show Word Count")
            print("4. Show Sentence Count")
            print("5. Show Number Count")
            print("6. Show Most Common Word(s)")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                report = processor.generate_report()
                print(report)
            elif choice == '2':
                print("Fixed Text:\n", processor.fixed_text)
            elif choice == '3':
                print(f"Word Count: {processor.number_of_words}")
            elif choice == '4':
                print(f"Sentence Count: {processor.number_of_sentences}")
            elif choice == '5':
                print(f"Number Count: {processor.count_of_numbers}")
            elif choice == '6':
                print(f"Most Common Word(s): {processor.most_common_words}")
            elif choice == '7':
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")
    except Exception as e:
        logger.error(f"Error: {e}")

if __name__ == "__main__":
    main()
