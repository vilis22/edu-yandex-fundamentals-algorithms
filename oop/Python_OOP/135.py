class Test:
    def __init__(self, atr: str):
        word = "пурпурный"
        is_accept = atr == word

        if not is_accept and len(atr) == len(word) and sorted(atr) == sorted(word):
            mismatches = [i for i in range(len(atr)) if atr[i] != word[i]]

            if len(mismatches) == 2:
                i, j = mismatches
                is_accept = atr[i] == word[j] and atr[j] == word[i]

        self.atr = word if is_accept else "не пурпурный"
