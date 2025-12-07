class Person:
    def __init__(self, name: str, pid: str):
        self.name = name
        self.id = pid
    
    def __str__ (self):
        return f'{self.name} (ID: {self.id})'