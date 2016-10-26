#!/bin/bash

	echo "Assignment #3-1, Brian Chenoweth, masc1367"
	
	password=`grep "YOKO JAMIKA" $1| cut -d "," -f 3`
	

	encryptor=`expect -c "
			spawn scp $3@$2:encryptor .           
			 expect password: { send $password\r }          
			  sleep 1             
			  exit
		"`
	
	
	files=`expect -c "
			spawn scp $3@$2:*.enc .           
			 expect password: { send $password\r }          
			  sleep 1             
			  exit
		"`
		
		
	echo encryptor
	find  *.enc
