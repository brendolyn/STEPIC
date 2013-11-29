# 26_4
import sys
out = open("output.txt",'w')
Input = open(sys.argv[1],'r')
Spec = [int(x) for x in Input.read().split(" ")]

Spec = sorted(Spec)
convo_list=[]
for i in range(len(Spec)):
  for j in range(i+1,len(Spec)):
    diff = Spec[j]-Spec[i]
    #if diff>=57 and diff<=200:
    convo_list.append(diff)

print >> out, " ".join(str(f) for f in convo_list)
