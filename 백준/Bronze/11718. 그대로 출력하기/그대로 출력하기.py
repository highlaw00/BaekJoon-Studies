# goal: print out as user input.

while True:
	try:
		print(input())
		# this loop will read every lines.
	except EOFError:
		# by the way if it detects EOF then it will stop.
		break