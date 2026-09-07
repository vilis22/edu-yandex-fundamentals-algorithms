class Human:
    def __init__(self, form: dict[str, int]):
        self.form = form


def func(human: Human):
    for characteristic in ("ярость", "депрессия", "безумие"):
        if human.form.get(characteristic, 0) > 3:
            human.form[characteristic] = 3
