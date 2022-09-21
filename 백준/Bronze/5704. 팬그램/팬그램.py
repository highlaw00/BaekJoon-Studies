d = dict()

while True:
    s = input()
    res = 'Y'
    if s == '*': break
    
    for i in range(26):
        d[chr(97+i)] = 0
        
    for curr in s:
        if 'a' <= curr <= 'z':
            d[curr] += 1
    
    for i in range(26):
        if d[chr(97+i)] == 0:
            res = 'N'
            
    print(res)