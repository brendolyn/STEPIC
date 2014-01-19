import sys

out=open("output.txt",'w')

Input=open(sys.argv[1],'r').read().split("\n")

text=Input[0].strip()
text=text[:-1]

from suffix_tree import SuffixTree
stree = SuffixTree(text)

max_len=0
for i in stree.preOrderNodes:
  if i.edgeLabel=="":  continue
  print >>out, i.edgeLabel

