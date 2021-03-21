class Nodo:
    def __init__(self, value=None):
        self.value = value
        self.up = self.right = self.down = self.left = None