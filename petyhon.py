def MinimumMneNaidy(Arra):
	masiv = Arra.split()

	minimum = masiv[0]
	for i in masiv:
		if int(i) < int(minimum):
			minimum = i
	return minimum

Arra = input(":")


print(MinimumMneNaidy(Arra))