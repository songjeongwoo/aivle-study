N=int(input())
cnt=0
d=N
while True :    
    a=d//10
    b=d%10
    c=(a+b)%10
    d=(b*10)+c
    cnt+=1
    if d==N:
        break
print(cnt)