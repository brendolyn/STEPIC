# 88_1
import sys

out=open("output.txt",'w')

Input=open(sys.argv[1],'r')
List=Input.read().strip()[1:(-1)].split(" ")

if List[0]=="+1":
  num=0
else:
  num=1

for i in range(1,len(List)):
  i1=int(List[i-1])
  i2=int(List[i])
  if i2-i1!=1:
    num+=1

if not List[-1]=="+"+str(len(List)):
  num+=1

print num
