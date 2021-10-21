import numpy as np


def threshold(x):
    """Функция активации"""
    t = 5  # порог
    if x >= t:
        return 1
    else:
        return 0


class Neuron:
    def __init__(self, w):
        self.w = w

    def y(self, x):  # Сумматор
        s = np.dot(self.w, x)
        return threshold(s)


if __name__ == '__main__':
    Xi = np.array([2, 0, 1, 3])  # входы
    Wi = np.array([7, 2, 4, 2])  # веса
    n = Neuron(Wi)
    print("Y =", n.y(Xi))