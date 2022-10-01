def change(n, s):
    res = ['', '', '']
    res[n-1] = s
    
    # 카멜로 변환
    if n != 1:
        tmp = '' + s[0].lower()
        for i in range(1, len(s)):
            if s[i-1] == '_':
                tmp = tmp[:-1]
                tmp += s[i].upper()
                continue
            else: tmp += s[i]
        res[0] = tmp
        
    if n != 2:
        tmp = '' + s[0]
        for i in range(1, len(s)):
            if 'A' <= s[i] <= 'Z':
                tmp += '_'
            tmp += s[i]
        tmp = tmp.lower()
        res[1] = tmp
        
    if n != 3:
        tmp = '' + s[0].upper()
        for i in range(1, len(s)):
            if s[i-1] == '_':
                tmp = tmp[:-1]
                tmp += s[i].upper()
                continue
            else: tmp += s[i]
        res[2] = tmp
    return res

idx, s = map(str,input().split())
idx = int(idx)
l = change(idx,s)

for sen in l: print(sen)