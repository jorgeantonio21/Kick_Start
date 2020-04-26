import numpy as np
import queue

class Node():
    def __init__(self, char, val, children):
        self.char = char
        self.val = val
        self.children = children
        
class Trie():
    def __init__(self):
        self.root = Node(char='', val=0, children=[])
        
    def insert(self, string):
        node = self.root
        node.val+=1
        for ch in string:
            child_found=False
            for nd in node.children:
                if ch == nd.char:
                    new_node=nd
                    new_node.val+=1
                    child_found = True
            if not(child_found):
                new_node=Node(char=ch, val=1, children=[])
                node.children+=[new_node]
            node=new_node
  

T = int(input())

for turn in range(T):
    N_K = [int(x) for x in input().split()]
    N = N_K[0]
    K = N_K[1]
    counter=0
    tree = Trie()
    print(tree.root.children)
    for i in range(N):
        tree.insert(str(input()))
    nodes = queue.Queue()
    for child in tree.root.children:
        nodes.put(child)
    while not(nodes.empty()):
        nd = nodes.get()
        counter += nd.val//K
        for child in  nd.children:
            nodes.put(child)
    print("Case #{}: {}".format(turn+1, counter)) 