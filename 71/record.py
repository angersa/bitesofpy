class RecordScore():
    """Class to track a game's maximum score"""

    def __init__(self):
        self._score = float('-inf')

    def __call__(self, score):
        self._score = max(self._score, score)
        return self._score


record = RecordScore()

print(record(10))
print(record(3))
print(record(12))