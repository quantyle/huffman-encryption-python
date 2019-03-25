import numpy as np


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


file = "probabilities.txt"
probabilities = {}  # a dictionary to hold codewords and their item

# read probabilities from probabilities.txt
with open(file) as fp:
    line = fp.readline()
    count = 0
    while line:
        line = line.replace('\n', '')
        if line != '':
            if line in probabilities:
                n = probabilities[line]
                n += 1
                probabilities[line] = n
            else:
                probabilities[line] = 1
        line = fp.readline()
        count += 1

print(probabilities)

stack = Stack()  # this will keep track of the two lowest values

p_sorted = sorted(probabilities, key=probabilities.get, reverse=True)

print(p_sorted)

print("stack: " + str(stack.items))
