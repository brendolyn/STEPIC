import sys

Input=open(sys.argv[1],'r').read().split("\n")
text=Input[0].strip()

out=open("output.txt",'w')

dualText=text+text
rotation=[]
for i in range(len(text)):
  rotation.append(dualText[i:(i+len(text))])
rotation=sorted(rotation)

print >>out, "".join([x[-1] for x in rotation])
