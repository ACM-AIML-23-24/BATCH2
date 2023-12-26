from collections import OrderedDict
ord_dict = OrderedDict()
n=int(input())
for _ in range(n):
    data = input().split()
    pr = int(data.pop())
    name = ' '.join(data)
    if name in ord_dict:
        ord_dict[name] += pr
    else:
        ord_dict[name] = pr

[print(item[0] + ' ' + str(item[1])) for item in ord_dict.items()]