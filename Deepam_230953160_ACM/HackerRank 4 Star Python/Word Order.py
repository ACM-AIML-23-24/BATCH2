n= int(input())
ctr = {}
lis_wrd = []

for i in range(n):
  word = input()
  lis_wrd.append(word)
  if word in ctr:
    ctr[word] += 1
  else:
    ctr[word] = 1
    
print(len(ctr))
print(' '.join([str(ctr[word]) for word in ctr]))
