import sys

global out
out=open("output.txt",'w')
class Node:
    def __init__(self,value):
        self.child={}
        self.value=value
    def addChild(self,edge,node):
        self.child[edge]=node

def show(node):
    global out
    if node.child=={}: return
    for i in node.child:
        print >>out, node.value,node.child[i].value,i
        show(node.child[i])

class Trie:
    def __init__(self):
        self.root=Node(1)
        self.num=1 #number of node
    def addString(self,Str):
        node=self.root
        for i in Str:
            if i not in node.child:
                self.num+=1
                node.child[i]=Node(self.num)
            node=node.child[i]

                
    def showTrie(self):
        show(self.root)


Input=open(sys.argv[1],'r').read().split("\n")

Strings=[x.strip() for x in Input]

trie=Trie()

for s in Strings:
    if s=="": continue
    trie.addString(s)

trie.showTrie()

            
            
          
