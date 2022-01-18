# 2884. 알람시계
#  "45분 일찍 알람 설정하기"

a, b = map(int, input().split())
if b >= 45:
    print(a, b-45)
elif (a == 0 and b < 45):
    print(a+23, 60-(45-b))
elif (a > 0 and b < 45):
    print(a-1, 60-(45-b))
    