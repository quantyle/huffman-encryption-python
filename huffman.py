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
print('nodes: ' + str(stack.items))
tree = []

count = 0
empty_nodes = [] #necessary to build decision tree viz
for item in stack.items:
    tree.append(sorted(stack.items[-2:]))
    if count == 0:
        empty_nodes = [None] * ( (len(stack.items) - 2) * 2)
    # pop the smallest two 
    n0 = stack.pop()
    n1 = stack.pop()
    n3 = n0 + n1
    nodes = sorted([n0, n1])

    #print("adding smallest nodes: " + str(nodes))
    
    if(n3 <= 1.0):
        if(n3 > stack.items[0]):
            insert_at = 0
            b = stack.items[:] 
            b[insert_at:insert_at] = [n3]
            stack.items = b
            
            #tree.append(stack.items)
        else: 
            insert_at = 1
            b = stack.items[:] 
            b[insert_at:insert_at] = [n3]
            stack.items = b
            #tree.append([n0,n1])
            #tree.append(stack.items)

        # if count == 0:
        #     empty_nodes = [None] * ( (len(stack.items) - 2) * 2)
        #     tree.append(empty_nodes) # padding nodes for tree
        #     tree.append(nodes)
        # else: 
        #     tree.append(nodes)
    print('nodes: ' + str(stack.items))
    count +=1

        #print("adding smallest nodes: [%f , %f] -->  [%f]" % (n0, n1, n3))
tree.append(sorted(stack.items[-2:]))
top_2 = stack.items[-2:]
top = top_2[0] + top_2[1]
tree.append([top])


#insert padding nodes


insert_at = 1
b = tree[:] 
b[insert_at:insert_at] = [empty_nodes]
tree = b

# append leftovers
#tree.append([stack.items[0]])
tree_2=[1.0, 0.6, 0.4, 0.4, 0.2, 0.2, 0.2, None, None, None, None, None, None, 0.1, 0.1]
tree = [j for sub in tree for j in sub]
tree = tree[::-1]

# tree = sorted(tree, reverse=True)
root = build(tree)
print(root)


