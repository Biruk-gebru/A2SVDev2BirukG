x=int(input())
a1=set(map(int,input().split()))
y=int(input())
a2=set(map(int,input().split()))
print(len(a1.difference(a2)))
