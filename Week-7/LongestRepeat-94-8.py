import sys



out=open("output.txt",'w')

Input=open(sys.argv[1],'r').read().split("\n")

text=Input[0].strip()

from suffix_tree import SuffixTree
stree = SuffixTree(text)

max_len=0
for i in stree.innerNodes:
  s=i.pathLabel
  if len(s) > max_len:
    max_len=len(s)
    longestRep=s

print >>out,longestRep
