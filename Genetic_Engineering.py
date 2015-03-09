#		SOLUTION


sequence = raw_input()
count = 1
answer = 0
length = len(sequence)
for i in range(length):
	if i+1 < length:
		if sequence[i] == sequence[i+1]:
			count = count + 1
		else:
			if count % 2 == 0:
				answer = answer + 1
				count = 1
			else:
				count = 1

print answer
