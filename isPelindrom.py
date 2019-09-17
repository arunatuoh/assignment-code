def isPelindrom(s):
	i = 0
	j = len(s)-1
	flag = False
	while i<= j:
		if s[i] != s[j]:
			continue
			flag = True
			break
		i = i+1
		j = j - 1
	if flag:
		print("NO")
	else:
		print("YES")

isPelindrom("JAHAJ")