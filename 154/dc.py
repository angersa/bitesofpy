from dataclasses import dataclass

@dataclass
class Bite:
    number: int
    title: str
    level: str

    def __init__(self, number, title, level='Beginner'):
        super().__init__()
        self.title = title.capitalize()
        self.number = number
        self.level = level

    def __lt__(self, other):
         return self.number < other.number

