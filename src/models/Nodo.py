from models import Nodo


class Nodo:
    def __init__(self, next: Nodo, data):
        self.next = next
        self.data = data
