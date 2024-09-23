class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __str__(self):
        return f"{self.name} - Typing: {self.typing}, Reflection: {self.reflection}, Year: {self.year}, Pointer Arithmetic: {self.pointer_arithmetic}"
