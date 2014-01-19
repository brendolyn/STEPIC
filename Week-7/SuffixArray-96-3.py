import sys

Input=open(sys.argv[1],'r')
out=open("output.txt",'w')

text=Input.read().strip()


suffixs=[]
for i in range(len(text)):
  suffixs.append(text[i:])
order=[i[0] for i in sorted(enumerate(suffixs), key=lambda x:x[1])]
print >>out,", ".join([str(x) for x in order])
