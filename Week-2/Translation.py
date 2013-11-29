import sys

table_file = open("RNA_codon_table_1.txt",'r')
out = open("output.txt",'w')
table={}
for l in table_file.read().split("\n"):
  l=l.strip().split(" ")
  if len(l)>1:
    table[l[0]]=l[1]
  else:
    table[l[0]]=""

Input = open(sys.argv[1])
seq = Input.read().strip()

pseq = ""
i = 0
stop = False
while (i<=len(seq)-3) and stop==False:
  aa = table[seq[i:(i+3)]]
  pseq += aa
  if aa=="":
    stop=True
  i+=3

print >> out, pseq
  


