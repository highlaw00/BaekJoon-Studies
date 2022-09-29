t = int(input())

for _ in range(t):
    fw, sw = map(str,input().split())
    flag = True
    fl, sl = [0 for _ in range(26)], [0 for _ in range(26)]
    
    if len(fw) != len(sw): 
        print('{} & {} are NOT anagrams.'.format(fw, sw))
        continue
    
    for l in fw:
        fl[ord(l) - ord('a')] += 1
    for l in sw:
        sl[ord(l) - ord('a')] += 1
    
    for i in range(26):
        if fl[i] != sl[i]: 
            flag = False
            break
    
    if flag: print('{} & {} are anagrams.'.format(fw, sw))
    else: print('{} & {} are NOT anagrams.'.format(fw, sw))
            