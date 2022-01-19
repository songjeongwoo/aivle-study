N=int(input())
a=list(map(int,input().split()))

M=max(a)
for i in range(len(a)):
    a[i]=a[i]/(M*100)

b=sum(a)
print((b/len(a))*10000)