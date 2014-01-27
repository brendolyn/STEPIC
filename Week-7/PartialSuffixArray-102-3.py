import sys

Input=open(sys.argv[1],'r').read().split('\n')
out=open("output.txt",'w')

text=Input[0].strip()
k=int(Input[1])


suffixs=[]
for i in range(len(text)):
  suffixs.append(text[i:])
order=[i[0] for i in sorted(enumerate(suffixs), key=lambda x:x[1])]

for i in range(len(order)):
  if order[i]%k==0:
    print >>out, '%d,%d'%(i,order[i])
