D = {'lower': 0, 'upper': 0, 'number': 0, 'blank': 0}

while True:
    try:
        s = input()
        for i in range(len(s)):
            if '0' <= s[i] <= '9':
                D['number'] += 1
            elif 'A' <= s[i] <= 'Z':
                D['upper'] += 1
            elif 'a' <= s[i] <= 'z':
                D['lower'] += 1
            else:
                D['blank'] += 1
        print('{} {} {} {}'.format(D['lower'], D['upper'], D['number'], D['blank']))
        D['blank'], D['lower'], D['number'], D['upper'] = 0, 0, 0, 0
    except:
        break