ab = input()
a_cnt = ab.count('a')
ans = 1001

for i in range(len(ab)):
    sub = ''
    if i + a_cnt >= len(ab):
        check = (i + a_cnt) % len(ab)
        sub = ab[i:] + ab[:check]
    else:
        sub = ab[i : i+a_cnt]
    b_cnt = sub.count('b')
    ans = min(ans, b_cnt)

print(ans)