strr = input()

# 문자열은 원형이라 처음과 끝이 이어진다,,,
# a 개수 세어주자

cnt = strr.count('a')

minn = float('INF')
strr += strr
for i in range(len(strr)-cnt-1):
    minn = min(minn, strr[i:i+cnt].count('b'))
print(minn)
