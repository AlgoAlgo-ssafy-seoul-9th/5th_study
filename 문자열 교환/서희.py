'''
a와 b로만 이루어진 문자열이 주어질 때,  a를 모두 연속으로 만들기 위해서 필요한 교환의 회수를 최소로 하는 프로그램을 작성하시오.

이 문자열은 원형이기 때문에, 처음과 끝은 서로 인접해 있는 것이다.

예를 들어,  aabbaaabaaba이 주어졌을 때, 2번의 교환이면 a를 모두 연속으로 만들 수 있다.

첫째 줄에 필요한 교환의 회수의 최솟값을 출력한다.

'''

S = input()
a = S.count('a')

ans = len(S)            # 전체문자열의 길이
for i in range(a-1, len(S)): # 두 번째 부분 문자열의 시작 위치
    ans = min(ans, S[i - a + 1:i+1].count('b'))

for i in range(0, a-1):     # 첫 번째 부분 문자열의 끝 위치
    ans = min(ans, (S[i-a+1:] + S[:i+1]).count('b'))

print(ans)