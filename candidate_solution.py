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

    def rec_eval(self, env:Dict) -> float:
        retval = 0
        # handle terminals
        if str(self.value) == self.symbol:
            # value is constant number:
            if type(self.value) == int or type(self.value) == float:    
                return float(self.value)
            # value is variable
            elif self.symbol in env.keys():         
                return float(env[self.symbol])
            # error: value is neither a constant number nor a variable defined in environment
            else:
                raise KeyError
        # handle operators
        if self.leftchild is not None:
            retval = self.leftchild.rec_eval(env)
        #
                


        #
        if self.righchild is not None:
            retval += self.righchild.rec_eval(env)



class Program:

    def __init__(self, config: Dict) -> None:
        """construct a random program tree using Terminals and Operators defined in config obj"""
        self.config = config
        self.root = Node(self.config)
    
    def __str__(self) -> str:
        """recursive string method is implemented in Node class"""
        if self.root is None:
            return "()"
        return self.root.rec_str()
    
    def eval(self, env:Dict) -> float:
        """recursive evaluation method is implemented in Node class"""
        return self.root.rec_eval(env)
        


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