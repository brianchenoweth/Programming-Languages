Assignment #5-1, Brian Chenoweth, masc1367

def Tokenize( filename ):
	file = open( filename, 'r')
	with open( filename, 'r') as f:
		content = f.readlines()
		brian = []
		for line in content:
			brian.append(line.split())
	return brian
