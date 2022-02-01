# 4344. 평균은 넘겠지
'''
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
'''

a = int(input())

for i in range(a):
    b = list(map(int, input().split()))
    c = (sum(b)-b[0])/b[0]
    d = 0
    for e in b[1:]:
        if e > c:
            d += 1
    print(f'{"%0.3f" % (d/b[0]*100)}%')