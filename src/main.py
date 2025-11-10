import sys
from src.word_pair_counter import count_word_pairs

def main():
    if len(sys.argv) != 5:
        print("Use: python -m src.main <file> <word1> <word2> <max distant>", file=sys.stderr)
        sys.exit(1)

    file_path = sys.argv[1]
    word1 = sys.argv[2]
    word2 = sys.argv[3]
    try:
        max_dist = int(sys.argv[4])
        if max_dist < 0:
            raise ValueError
    except ValueError:
        print("Max distant should be a non-negative number", file=sys.stderr)
        sys.exit(1)

    try:
        res = count_word_pairs(file_path, word1, word2, max_dist)
        print(res)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

