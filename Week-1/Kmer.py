import sys

Input=open(sys.argv[1])
Input=Input.read().split("\n")
String=Input[0]
k=int(Input[1])

kmer={}
Max=0
for i in range(len(String)-k+1):
    sub=String[i:(i+k)]
    if sub in kmer:
        kmer[sub]+=1
        if Max<kmer[sub]:
            Max=kmer[sub]
    else:
        kmer[sub]=0

Max_list = filter(lambda x: kmer[x]==Max, kmer.keys())

print " ".join(Max_list)
    
