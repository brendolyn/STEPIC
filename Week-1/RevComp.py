def reverse_complement(s):
    complements = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join([complements[c] for c in reversed(s)])


import sys
Input=open(sys.argv[1])
String=Input.read().strip()
out = open("output.txt",'w')
print >>out,reverse_complement(String)
