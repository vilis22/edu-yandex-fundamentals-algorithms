class Button:
    def __init__(self, letter: str):
        self.letter = letter


lst = [Button(letter) for letter in "abcdefghijklmnopqrstuvwxyz"]
