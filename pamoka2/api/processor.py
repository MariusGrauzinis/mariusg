import re
from collections import Counter
from dataclasses import dataclass
from typing import List
import logging
import json

logger = logging.getLogger("TextProcessor")
logger.setLevel(logging.DEBUG)
if not logger.handlers:
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
        return json.dumps(self.__dict__, indent=2)

    def __repr__(self) -> str:
        return f"<TextReport with {self.number_of_words} words>"

class TextProcessor:
    def __init__(self, raw_text: str) -> None:
        self.raw_text = raw_text
        logger.debug("TextProcessor initialized")

    @staticmethod
    def clean_text(text: str) -> str:
        logger.info("Cleaning text")
        text = re.sub(r',(\S)', r', \1', text)
        sentences = re.split(r'(?<=[.!?])\s+', text.strip())
        cleaned_sentences = []
        for s in sentences:
            s = s.strip()
            if s:
                cleaned_sentences.append(s[0].upper() + s[1:] if len(s) > 1 else s.upper())
        return ' '.join(cleaned_sentences)

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
    def most_common_words_list(self) -> List[str]:
        counts = Counter(word.lower() for word in self.words if not word.isdigit())
        max_freq = max(counts.values(), default=0)
        return [w for w, c in counts.items() if c == max_freq]

    @property
    def most_common_words(self) -> str:
        return ', '.join(self.most_common_words_list)

    def generate_report(self) -> TextReport:
        return TextReport(
            fixed_text=self.fixed_text,
            number_of_words=self.number_of_words,
            number_of_sentences=self.number_of_sentences,
            count_of_numbers=self.count_of_numbers,
            most_common_words=self.most_common_words
        )
