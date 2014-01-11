# 71_8

import sys

out=open("output.txt",'w')

Input=open(sys.argv[1],'r').read().split("\n")
N = int(Input[0])
Coins = [int(i) for i in Input[1].split(",")]

MinNum = [N]*(N+1)
MinNum[0] = 0

for i in range(N+1):
  for j in Coins:
    if i >= j:
      if MinNum[i-j]+1 < MinNum[i]:
        MinNum[i] = MinNum[i-j]+1

print MinNum[N]
