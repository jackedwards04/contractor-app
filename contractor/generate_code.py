import random, string
def newCode():
	return(''.join(random.choices(string.ascii_letters, k=8)).upper())

