s, k, h = map(int,input().split())

if (s + k + h >= 100):
    print("OK")
else:
    worst = min(s,k,h)
    if worst == s:
        print("Soongsil")
    elif worst == k:
        print("Korea")
    else:
        print("Hanyang")