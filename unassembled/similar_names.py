import sys
from collections import defaultdict


def main():
    input_data = sys.stdin.read().split()
    words = input_data[1:]
    patterns = defaultdict(int)
    word_counts = defaultdict(int)
    word_length = len(words[0])

    for word in words:
        word_counts[word] += 1
        for i in range(word_length):
            pattern = word[:i] + "*" + word[i + 1 :]
            patterns[pattern] += 1

    total_pairs = 0

    # Если шаблон встретился K раз, то количество пар = K * (K - 1) // 2
    for count in patterns.values():
        total_pairs += count * (count - 1) // 2

    # Убираем полностью одинаковые слова как "подходящие".
    for word, count in word_counts.items():
        if count > 1:
            duplicates_pairs = count * (count - 1) // 2
            total_pairs -= duplicates_pairs * word_length

    print(total_pairs)


if __name__ == "__main__":
    main()
