###############################################
# person.py
###############################################
class Person:
    def __init__(self, name, pid):
        self.name = name
        self.pid = pid

    def __str__(self):
        return f'Person(name={self.name}, id={self.pid})'
