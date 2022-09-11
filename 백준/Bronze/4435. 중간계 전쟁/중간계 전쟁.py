input = __import__('sys').stdin.readline
t = int(input())

for i in range(t):
    ghobit, ghuman, gelf, gdwarf, geagle, gmagician = map(int,input().split())
    sorc, shuman, swarg, sgoblin, shigh, stroll, smagician = map(int, input().split())
    gsum = ghobit + 2 * ghuman + 3 * gelf + 3 * gdwarf + 4 * geagle + 10 * gmagician
    ssum = sorc + 2 * shuman + 2 * swarg + 2 * sgoblin + 3* shigh + 5 * stroll + 10 * smagician
    
    if gsum > ssum:
        print("Battle {}: Good triumphs over Evil".format(i + 1))
    elif gsum < ssum:
        print("Battle {}: Evil eradicates all trace of Good".format(i + 1))
    else:
        print("Battle {}: No victor on this battle field".format(i + 1))