import re
from typing import Iterator

def tokenize(text: str) -> Iterator[str]:
    for match in re.finditer(r'\b\w+\b', text):
        yield match.group().lower()

def count_word_pairs(file_path: str, word1: str, word2: str, max_dist: int) -> int:
    word1 = word1.lower()
    word2 = word2.lower()
    count = 0
    word_index = 0
    last_word1_pos = None

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                for token in tokenize(line):
                    if token == word1:
                        last_word1_pos = word_index
                    elif token == word2 and last_word1_pos is not None:
                        distance = word_index - last_word1_pos - 1
                        if 0 <= distance <= max_dist:
                            count += 1
                            last_word1_pos = None
                    word_index += 1
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except UnicodeDecodeError:
        raise ValueError(f"Can't read the file like text: {file_path}")

    return count
