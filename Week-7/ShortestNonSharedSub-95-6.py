import sys

out=open("output.txt",'w')

Input=open(sys.argv[1],'r').read().split("\n")

text1=Input[0].strip()
text2=Input[1].strip()

shared=True
i=1
while shared:
  for j in range(len(text1)-i):
    s=text1[j:(j+i+1)]
    if text2.find(s)==-1:
      shared=False
      unsharedS=s
      break
  i+=1

print unsharedS
