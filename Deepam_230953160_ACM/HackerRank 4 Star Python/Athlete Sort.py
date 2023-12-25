def sorting(k,arr):
     arr.sort(key = lambda x: x[k])
     for i in arr:
         print(' '.join(str(x) for x in i))
    
if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
    sorting(k,arr)