import typing
import numpy as np
from matplotlib import pyplot as plt
import random



conf = {
    "Operators": [
        lambda a,b : a+b,
        lambda a,b : a-b,
        lambda a,b : a*b,
        lambda a,b : a/b if b != 0 else 1000000000,
        lambda a,b : a**b 
    ],
    "Terminals": ["x"]
}

class Node:
    def __init__(self, config) -> None:

        if random.random() > .5:    
            # pick operator
            self.value = random.choice(config["Operators"])
            self.leftchild = Node(config)
            self.righchild = Node(config)
        else:                       
            # pick terminal
            self.value = random.choice(config["Terminals"])
            self.leftchild = None
            self.righchild = None


class Program:
    def __init__(self, config: typing.Dict) -> None:
        self.config = config
        self.root = Node(self.config)



class Testcase:
    def __init__(
        self, f: callable, xmin: int, xmax: int, n_sample: int, n_ctrl: int
    ) -> None:

        self.f = f
        self.n_samle = n_sample
        self.n_ctrl = n_ctrl
        self.xrange = (xmin, xmax)

        self.X = np.random.randint(xmin, xmax, n_sample)
        self.Y = f(self.X)

    def draw(self, filename: str):
        fig, ax = plt.subplots()
        ax.scatter(self.X, self.Y)
        fig.savefig(f"{filename}.png")

    def compute_fitness(program:Program):
        pass




if __name__ == "__main__":
    tc = Testcase(lambda x: x * x, -10, 10, 20, 100)
    tc.draw("test.png")
