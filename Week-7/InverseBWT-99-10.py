import sys

Input=open(sys.argv[1],'r').read().split("\n")
text=Input[0].strip()

out=open("output.txt",'w')


#==============================================
# from http://pastebin.com/7LPCv9C3
def follow(perm, end):
  i = perm[end]
  while i != end:
    yield i
    i = perm[i]
 
def inv_bwt(s):
  perm = sorted(range(len(s)), key=lambda x: s[x])
  return ''.join(s[i] for i in follow(perm, s.index('$')))
#===============================================
print >> out, inv_bwt(text)+"$"
