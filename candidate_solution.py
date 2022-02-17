from typing import Dict
from random import choice, random


class Node:
    def __init__(self, config: Dict) -> None:
        """construct a randomized Node, works recursive for operator nodes"""
        if random() > 0.5:
            # pick an operator
            try:
                self.value, self.symbol = choice(config["Operators"])
                # recursive calls for child nodes
                self.leftchild = Node(config)
                self.righchild = Node(config)
            except KeyError:
                raise KeyError
        else:
            # pick a terminal
            try:
                self.value = choice(config["Terminals"])
                self.symbol = str(self.value)
            except KeyError:
                raise KeyError
            self.leftchild = None
            self.righchild = None

    def rec_str(self) -> str:
        """recursive implementation of program's string method"""
        s = ""
        if self.leftchild is not None:
            s = self.leftchild.rec_str() + s
        s += self.symbol
        if self.righchild is not None:
            s += self.righchild.rec_str()
        return f"({s})"

    def rec_eval(self, env: Dict) -> float:
        """
        recursive implementation of Program's evaluation method,
        variables defined in Terminal Set must also be assigned in env dictionary
        """
        # handle terminals
        if str(self.value) == self.symbol:
            # value is constant number:
            if (type(self.value) == int) or (type(self.value) == float):
                return float(self.value)
            # value is variable
            elif self.symbol in env.keys():
                return float(env[self.symbol])
            # error: value is neither a constant number nor a variable defined in environment
            else:
                raise KeyError
        # handle operators
        return float(
            self.value(self.leftchild.rec_eval(env), self.righchild.rec_eval(env))
        )


class Program:
    def __init__(self, config: Dict) -> None:
        """
        construct a random tree representing a Programm instance using the Terminals and Operators defined in <config> dictionary
        """
        self.config = config
        self.root = Node(self.config)

    def __str__(self) -> str:
        """recursive string method is implemented in Node class"""
        if self.root is None:
            return "()"
        return self.root.rec_str()

    def eval(self, env: Dict) -> float:
        """recursive evaluation method is implemented in Node class"""
        return self.root.rec_eval(env)


if __name__ == "__main__":

    conf = {
        "Operators": [
            [lambda a, b: a + b, "+"],  # [callable, symbolic representation]
            [lambda a, b: a - b, "-"],
            [lambda a, b: a * b, "*"],
            [lambda a, b: a / b if b != 0 else 99999999, "/"],
            [lambda a, b: a ** b, "^"],
        ],
        "Terminals": ["uv", 1, 2],
    }

    env = {"uv": 2}

    p = Program(conf)
    print(p)
    print(p.eval(env))
