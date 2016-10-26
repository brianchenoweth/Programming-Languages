import sys
from prog5-1 import *
from prog5-2 import *

print ("Assignment #5-3, Brian Chenoweth, masc1367")

chenoweth = Tokenize (sys.argv[1])


for line in chenoweth:
	mylist = []
	for part in line:
		try:
 			int(part)
			hello = LiteralIntToken(part)
		except:
			hello = NameToken(part)
		mylist.append(day)
	print(' '.join([bye.GetElementType() for bye in mylist]))
