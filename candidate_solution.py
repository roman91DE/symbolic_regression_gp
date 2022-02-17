from re import S
from typing import Dict
from random import choice, random

class Node:
    def __init__(self, config:Dict) -> None:

        if random() > 0.5:
            # pick operator
            try:
                self.value, self.symbol = choice(config["Operators"])
                self.leftchild = Node(config)
                self.righchild = Node(config)
            except KeyError:
                raise KeyError
        else:
            # pick terminal
            try:
                self.value = choice(config["Terminals"])
                self.symbol = str(self.value)
            except KeyError:
                raise KeyError
            self.leftchild = None
            self.righchild = None
    
    def rec_str(self) -> str:
        s = ""
        if self.leftchild is not None:
            s = self.leftchild.rec_str() + s
        s += self.symbol
        if self.righchild is not None:
            s += self.righchild.rec_str()
        return f"({s})"



class Program:

    def __init__(self, config: Dict) -> None:
        self.config = config
        self.root = Node(self.config)
    
    def __str__(self) -> str:
        if self.root is None:
            return "()"
        return self.root.rec_str()
        


if __name__ == "__main__":

    conf = {
        "Operators": [
            [lambda a, b: a + b, "+"],
            [lambda a, b: a - b, "-"],
            [lambda a, b: a * b, "*"],
            [lambda a, b: a / b if b != 0 else 99999999, "/"],
            [lambda a, b: a ** b, "^"]
        ],
        "Terminals": ["uv", 1, 2],
    }

    p = Program(conf)
    print(p)