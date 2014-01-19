import sys

out=open("output.txt",'w')

Input=open(sys.argv[1],'r').read().split("\n")

text1=Input[0].strip()
text2=Input[1].strip()

from suffix_tree import GeneralisedSuffixTree
stree = GeneralisedSuffixTree([text1,text2])

max_len=0
for shared in stree.sharedSubstrings():
  seq,start,stop=shared[0]
  if (stop-start)> max_len:
    max_len=stop-start
    longestSS=stree.sequences[seq][start:stop]
print >>out, longestSS

