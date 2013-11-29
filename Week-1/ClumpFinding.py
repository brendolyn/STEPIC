import sys

Out=open("output.txt",'w')
Input=open(sys.argv[1])
Input=Input.read().split("\n")
String=Input[0]
if len(sys.argv)<=2:
    parameters=Input[1].split(" ")
    k=int(parameters[0])
    L=int(parameters[1])
    t=int(parameters[2])
else:
    k=int(sys.argv[2])
    L=int(sys.argv[3])
    t=int(sys.argv[4])

print "parameters: ",k,L,t
kmer={}
for i in range(len(String)-k+1):
    sub=String[i:(i+k)]
    if sub in kmer:
        kmer[sub].append(i)
    else:
        kmer[sub]=[i]

results=[]
for s in kmer:
    if len(kmer[s])<t: continue
    for j in range(len(kmer[s])-t+1):
        if kmer[s][j+t-1]-kmer[s][j]<=L-k:
            results.append(s)
            break
print len(results)
print >>Out," ".join(results)
