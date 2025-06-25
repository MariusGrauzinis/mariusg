# api/text_processor.py
import re
from collections import Counter
from dataclasses import dataclass, asdict
from typing import List

@dataclass
class TextReport:
    fixed_text: str
    number_of_words: int
    number_of_sentences: int
    count_of_numbers: int
    most_common_words: str

class TextProcessor:
    def __init__(self, raw_text: str) -> None:
        self.raw_text = raw_text

    def clean_text(self, text: str) -> str:
        text = re.sub(r',(\S)', r', \1', text)
        sentences = re.split(r'(?<=[.!?])\s+', text.strip())
        cleaned = [s[0].upper() + s[1:] if len(s) > 1 else s.upper() for s in sentences if s]
        return ' '.join(cleaned)

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
        return len([w for w in self.words if w.isdigit()])

    @property
    def most_common_words(self) -> str:
        counts = Counter(w.lower() for w in self.words if not w.isdigit())
        if not counts:
            return ''
        max_freq = max(counts.values())
        return ', '.join([w for w, c in counts.items() if c == max_freq])

    def generate_report(self) -> TextReport:
        return TextReport(
            fixed_text=self.fixed_text,
            number_of_words=self.number_of_words,
            number_of_sentences=self.number_of_sentences,
            count_of_numbers=self.count_of_numbers,
            most_common_words=self.most_common_words
        )
