import sys

out=open("output.txt",'w')
Input=open(sys.argv[1],'r').read().split("\n")
text=Input[0].strip()
Strings=[x.strip() for x in Input[1:]]


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

    def Match(self,text):
        node=self.root
        i=0
        while (node.child.has_key(text[i])):
            node=node.child[text[i]]
            i+=1
            if i>=len(text): break
        if node.child=={}:
            return text[:i]
        else:
            return "None"
            
    def showTrie(self):
        show(self.root)


trie=Trie()

min_len=len(text)
for s in Strings:
    if s=="": continue
    trie.addString(s)
    min_len=min(len(s),min_len)

for i in range(len(text)-min_len+1):
    if trie.Match(text[i:])!="None":
        print >>out, i,
