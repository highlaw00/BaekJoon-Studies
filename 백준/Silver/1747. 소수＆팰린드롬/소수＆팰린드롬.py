import math

n = int(input())
temp = n
if temp == 1: temp += 1

while True:
    # 소수 판별
    isPrime = True
    for i in range(2, int(math.sqrt(temp)) + 1):
        if temp % i == 0:
            isPrime = False
            break
    
    if not isPrime:
        temp += 1
        continue

    # 팰린드롬 확인
    word = str(temp)
    isPalindrome = True
    for i in range(0, len(word) // 2):
        if word[i] != word[len(word) - 1 - i]:
            isPalindrome = False
            break
    
    if not isPalindrome:
        temp += 1
        continue

    ans = temp
    break

print(ans)