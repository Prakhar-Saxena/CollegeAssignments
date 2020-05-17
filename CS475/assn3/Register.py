
def valueToBinary(value):
    return bin(value)

class Register:
    # has to contain bits and the value
    def __init__(self):
        self.bits = (0, 0, 0, 0, 0, 0, 0, 0)
        self.value = 0

    def setValue(self, value):
        if type(value) != int:
            return None
        self.value = value
