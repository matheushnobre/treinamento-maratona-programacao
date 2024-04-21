while True:
	try:
		l = int(input())
		ll = [int(i) for i in input().split()]
		ll.sort()

		v = ll[-1]
		if v < 10:
			print(1)
		elif v < 20:
			print(2)
		else:
			print(3)
	except EOFError:
		break