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