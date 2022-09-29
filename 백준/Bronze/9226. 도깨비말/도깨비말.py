word = ''
while True:
    word = input()
    if word == '#': break
    cons = ['a','e','i','o','u']
    
    for char in word:
        if char not in cons:
            # 자음인 경우 단어의 맨 뒤로 보내버린다.
            word = word[1:] + word[0]
        else: break
    
    print(word + 'ay')