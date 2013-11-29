import sys

Input=open(sys.argv[1])
Input=Input.read().split("\n")
Pattern=Input[0]
text=Input[1]
print len(text)

indexs=[]
for i in range(len(text)-len(Pattern)+1):
  if text[i:(i+len(Pattern))]==Pattern:
    indexs.append(i)
out = open("output.txt",'w')
print >> out, " ".join(str(f) for f in indexs)
