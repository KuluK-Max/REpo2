
Arra = input(":")

masiv = Arra.split()

minimum = masiv[0]
for i in masiv:
	if int(i) < int(minimum):
		minimum = i
print(minimum)