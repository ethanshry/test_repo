with open ('./out.txt', 'w') as fl:
	for i in range(0,10000):
		fl.write(str(i))
		fl.write('\n')
