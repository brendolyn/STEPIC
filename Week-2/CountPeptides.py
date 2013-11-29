import sys
out = open("output.txt",'w')
table_file = open("integer_mass_table.txt",'r')
table={}
for l in table_file.read().split("\n"):
  l=l.strip().split(" ")
  table[l[0]]=int(l[1])

value = [table[x] for x in table]
value = set(value)
def Count_dp(m):
  count=[0]*(m+1)
  count[0]=1
  for i in range(57,m+1):
    for j in value:
      if (i-j<0) : continue
      count[i]+=count[i-j]
  return count[m]
       
print Count_dp(int(sys.argv[1]))
    
