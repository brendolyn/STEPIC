import sys
out = open("output.txt",'w')
table_file = open("integer_mass_table.txt",'r')
table={}
for l in table_file.read().split("\n"):
  l=l.strip().split(" ")
  table[l[0]]=int(l[1])
    
Input = open(sys.argv[1])
seq = Input.read().strip()
value = [table[x] for x in list(seq)]

spec = [0]
for i in range(len(seq)):
  v=0
  for j in range(len(seq)-1):
    v+=value[(i+j)%len(seq)]
    spec.append(v)
spec.append(sum(value))

print >>out, " ".join(str(f) for f in sorted(spec))
    
  

