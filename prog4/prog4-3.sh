#!/bin/bash
echo "Assignment #4-3, Brian Chenoweth, masc1367"


gcc prog5-1.c -llua -lm -L /home/ma/j/lindenea/lua/lib -I /home/ma/j/lindenea/lua/headers/ -R /home/ma/j/lindenea/lua/lib

	./a.out $1 > results.txt
	
if cmp -s results.txt $2
	then 
		echo "Passed Test"
	else 
		echo "Failed Test"
fi
