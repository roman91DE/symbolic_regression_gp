import typing
import numpy as np
from matplotlib import pyplot as plt
import candidate_solution


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

    def compute_fitness(program: candidate_solution.Program):
        pass


if __name__ == "__main__":

    tc = Testcase(lambda x: x * x, -10, 10, 20, 100)
    tc.draw("test.png")
