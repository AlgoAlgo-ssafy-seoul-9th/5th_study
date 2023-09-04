# 5th_study

[백준 문제집 링크](https://www.acmicpc.net/workbook/view/16692)

[프로그래머스 문제](https://school.programmers.co.kr/learn/courses/30/lessons/118668)

<br/>
<br/>
<br/>

## [코딩 테스트 공부](./코딩%20테스트%20공부/)

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

### [민웅](./코딩%20테스트%20공부/민웅.py)

```py

```

### [병국](./코딩%20테스트%20공부/병국.py)

```py

```

### [상미](./코딩%20테스트%20공부/상미.py)

```py

```

### [성구](./코딩%20테스트%20공부/성구.py)

```py

```

</div>
</details>

<br/>
<br/>
<br/>

## [수 이어 쓰기](./수%20이어%20쓰기/)

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

### [민웅](./수%20이어%20쓰기/민웅.py)

```py
# 1515_수 이어쓰기_continuing numbers
import sys
input = sys.stdin.readline

number = input().rstrip()
length = len(number)

cnt = 1

while True:
    if length == 0:
        break

    check = str(cnt)
    l = len(check)

    for i in range(l):
        if length and number.startswith(check[i]):
            number = number[1:]
            length -= 1

    cnt += 1

print(cnt-1)
```

### [병국](./수%20이어%20쓰기/병국.py)

```py
tmp = input()
i = 0

while True:
    i += 1
    num = str(i) # num : 찾는 수
    while len(num) > 0 and len(tmp) > 0: # tmp와 num이 비어있지않을때만
        if num[0] == tmp[0]: # 같으면,,
            tmp = tmp[1:] # 한칸씩 땡긴다,,,,112 > 12 > 2
        num = num[1:] # tmp 다 땡기고 나면 num 땡기기
    if tmp == '': # tmp 이제 없으면,,
        print(i)
        break
```

### [상미](./수%20이어%20쓰기/상미.py)

```py

```

### [성구](./수%20이어%20쓰기/성구.py)

```py
# 1515 수 이어 쓰기
import sys
from collections import deque

input = sys.stdin.readline
n = deque(list(input().strip()))

index = 0

while n:
    index += 1
    nums = deque(list(str(index)))
    while nums and n:
        # 처음 자리 수부터 확인
        if nums[0] == n[0]:
            # 만약 첫자리가 같다면 다음 자리수 확인을 위한 입력값에서 하나 빼기
            n.popleft()
        # 앞자리부터 빼면서 확인
        nums.popleft()
print(index)

```

</div>
</details>

<br/>
<br/>
<br/>

## [문자열 교환](./문자열%20교환/)

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

### [민웅](./문자열%20교환/민웅.py)

```py
# 1522_문자열교환_string exchange
import sys
input = sys.stdin.readline

init_value = input().rstrip()

tail = init_value.count('a')
left = init_value[:tail]

new_str = init_value+left

start = 0
ans = float('inf')
for i in range(len(init_value)):
    temp = new_str[i:i+tail]
    check = temp.count('b')
    if check < ans:
        ans = check

print(ans)
```

### [병국](./문자열%20교환/병국.py)

```py
# 98% 오답
strr = input()

# 문자열은 원형이라 처음과 끝이 이어진다,,,
# a 개수 세어주자

cnt = strr.count('a')

minn = float('INF')
strr += strr
for i in range(len(strr)-cnt-1):
    minn = min(minn, strr[i:i+cnt].count('b'))
print(minn)


```

### [상미](./문자열%20교환/상미.py)

```py

```

### [성구](./문자열%20교환/성구.py)

```py
# 1522 문자열 교환
import sys
from collections import deque

input = sys.stdin.readline

s = input().strip()
cnt = 0
# 초기 a 갯수 구하기
for i in s:
    if i == "a":
        cnt += 1
left, right = 0, cnt
# a를 한 곳으로 모으기 위해서는 갯수만큼 리스트 범위를 정함
# 정한 범위 내에서 b의 갯수가 바꾸는 수
# 초기 b의 개수가 minV 초기 값
b_count = 0
for b in s[left:right]:
    if b == "b":
        b_count += 1
minV = b_count
# 윈도우 슬라이싱을 통해 옮기는 횟수의 최소 구하기
while left < len(s):
    if s[left] == "b":
        b_count -= 1
    #  원형 큐 조심
    if s[right % len(s)] == "b":
        b_count += 1
    left += 1
    right = (right + 1) % len(s)
    minV = min(minV, b_count)
print(minV)

```

</div>
</details>

<br/>
<br/>
<br/>

## [가희와 탑](./가희와%20탑/)

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

### [민웅](./가희와%20탑/민웅.py)

```py
# 24337_가희와 탑_Gahee and tower
import sys
from collections import deque
input = sys.stdin.readline

N, a, b = map(int, input().split())
ans = deque()
if a >= b:
    for i in range(1, a+1):
        ans.append(i)
    if (N-a) >= b:
        temp = ans.popleft()
        for k in range(N-b-a+1):
            ans.appendleft(1)
        ans.appendleft(temp)
    for j in range(b-1, 0, -1):
        ans.append(j)
else:
    for i in range(b, 0, -1):
        ans.append(i)
    for j in range(a-1, 0, -1):
        ans.appendleft(j)
    if (N-a-b) >= 0:
        temp = ans.popleft()
        for k in range(N-b-a+1):
            ans.appendleft(1)
        ans.appendleft(temp)

if len(ans) > N:
    print(-1)
else:
    print(*ans)
```

### [병국](./가희와%20탑/병국.py)

```py

```

### [상미](./가희와%20탑/상미.py)

```py

```

### [성구](./가희와%20탑/성구.py)

```py

```

</div>
</details>

<br/>
<br/>
<br/>
