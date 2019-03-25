import numpy as np
from binarytree import build

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
probabilities = []

with open(file) as fp:
    line = fp.readline()
    count = 0
    while line:
        line = line.replace('\n', '').strip()
        if line: 
            #print("line %s" % line)
            prob = float(line)
            probabilities.append(prob)
        line = fp.readline()
        count += 1

probabilities = sorted(probabilities, key=float, reverse=True)
stack = Stack()
stack.items = probabilities
print(stack.items)
tree = []


for item in stack.items:
    # pop the smallest two 
    n0 = stack.pop()
    n1 = stack.pop()
    n3 = n0 + n1

    if(n3 < 1.0):
        if(n3 > stack.items[0]):
            insert_at = 0
            b = stack.items[:] 
            b[insert_at:insert_at] = [n3]
            stack.items = b

            print(stack.items)
            print("..[%f , %f]" % (n0, n1))
            tree.append([n0,n1])
            #tree.append(stack.items)
        else: 
            insert_at = 1
            b = stack.items[:] 
            b[insert_at:insert_at] = [n3]
            stack.items = b
            print(stack.items)
            print("...[%f , %f]" % (n0, n1))
            tree.append([n0,n1])
            #tree.append(stack.items)

#append leftovers
tree.append([stack.items[0]])
print(tree)
tree = [j for sub in tree for j in sub]
tree = tree[::-1]
print(tree)
# tree = sorted(tree, reverse=True)
root = build(tree)
print(root)


