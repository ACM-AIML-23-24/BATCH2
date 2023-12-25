from collections import namedtuple
n=int(input())
field=input().split()
sum=0
for _ in range(n):
    stud=namedtuple('student',field)
    MARKS,CLASS,NAME,ID=input().split()
    student=stud(MARKS,CLASS,NAME,ID)
    sum+=int((student.MARKS))
print((sum/n))