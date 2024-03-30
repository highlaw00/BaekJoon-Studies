def check_palindrome(word, left, right, del_cnt):
    result = 0
    while left <= right:
        if word[left] == word[right]:
            left += 1
            right -= 1
            continue
        # 이미 한 번 다른 글자 삭제한 경우
        if del_cnt >= 1:
            result = 2
            break
        # 왼쪽 글자를 지웠을 때의 팰린드롬 여부
        result_left_del = check_palindrome(word, left + 1, right, del_cnt + 1)
        # 오른쪽 글자를 지웠을 때의 팰린드롬 여부
        result_right_del = check_palindrome(word, left, right - 1, del_cnt + 1)

        if result_left_del == 0 or result_right_del == 0:
            result = 1
            break
        else: 
            result = 2
            break
    return result

for _ in range(int(input())):
    word = input()
    left = 0
    right = len(word) - 1
    del_cnt = 0
    print(check_palindrome(word, left, right, del_cnt))