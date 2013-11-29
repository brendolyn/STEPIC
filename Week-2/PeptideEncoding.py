import sys

table_file = open("RNA_codon_table_1.txt",'r')
out = open("output.txt",'w')
table={}
for l in table_file.read().split("\n"):
  l=l.strip().split(" ")
  l[0] = l[0].replace("U","T")
  if len(l)>1:
    table[l[0]]=l[1]
  else:
    table[l[0]]=""

Input = open(sys.argv[1])
Input = Input.read().split("\n")
if len(Input)==2:
  seq = Input[0]
  Pep = Input[1]
else:
  seq = "".join(Input)
  Pep = "VKLFPWFNQY"

def reverse_complement(s):
    complements = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join([complements[c] for c in reversed(s)])

seq_rc = reverse_complement(seq)

def translation(seq):
  pseq = ""
  i = 0
  stop = False
  while (i<=len(seq)-3) and stop==False:
    aa = table[seq[i:(i+3)]]
    pseq += aa
    if aa=="":
      stop=True
    i+=3
  return pseq

for i in range(len(seq)-3*len(Pep)+1):
  temp_pep1 = translation(seq[i:(i+3*len(Pep))])
  temp_pep2 = translation(reverse_complement(seq[i:(i+3*len(Pep))]))
  if (temp_pep1 == Pep) or (temp_pep2 == Pep):
    print >> out, seq[i:(i+3*len(Pep))]
  if i%100000 == 0:
    print >>sys.stderr,"Processing %d of %d. \r"%(i,len(seq)),
 

