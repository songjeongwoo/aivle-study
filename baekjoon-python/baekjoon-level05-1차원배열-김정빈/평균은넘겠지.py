C=int(input())
for _ in range(C):
    a = list(map(int,input().split()))
    avg = sum(a[1:])/a[0]
    count = 0

    for score in a[1:]:
        if score>avg:
            count+=1
    rate = count/a[0]*100
    round(rate, 3)
    print(f'{rate:.3f}%')