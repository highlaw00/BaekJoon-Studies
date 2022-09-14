sentence = input()
n = len(sentence)
i = 0

while n > i:
	print(sentence[i], end = '')
	i += 1
	if i % 10 == 0:
		if i == n:
			break
		else:
			print()