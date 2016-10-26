Your Job at CompilerCo Inc has been terrible thus far. Your boss has been asking you to implement and fix a surprisingly large 
number of memory leaks in the compiler that your company charges large amounts of money for. Thus, when offered the task of writing 
the basic tools for a new language that is being developed in-house you have jumped at the prospect. To avoid the memory leaks of C, 
you have decided to write all of your basic tools in python.

To get started you are going to write a function called Tokenize that will take a single input argument. This input argument is 
going to be the filename of a text file that will be in the same directory. Your function will read in the file and tokenize each
line from the file. This function will return a list of lists (think multidimensional array). The outer list will contain a list for 
each line in the file. Each of the inner lists will be that line from the file split into ‘tokens’. For the first section a ‘token’ 
is simply a string. Your function should split the line based on spaces. You should assume that the input is valid.


The second step of this assignment is to write a set of classes for the basic elements that will make up the language. To do this 
you will define a Token class, a LiteralIntToken class and a NameToken class. For the assignment we will not distinguish between 
operators and Names, but the extra credit is to include an OperatorToken class that will be created for particular set of operators.
These classes will have a constructor and two functions. The constructor will take a single argument (other than the self reference) 
that will be the string representation of the token (this is the part we have split in the first section). The first function will be 
the GetStringValue() function will return the string representation that was stored by the constructor. The second function will be 
the GetElementType() function which will return “Unknown” for the Token class, “Literal-Int” for the LiteralIntToken class and 
“Name” for the NameToken class.

The third and final step is to put these two pieces together. You will write a python script called prog5-3.py that will take a single 
command line argument which will be the name of a file. Your script will then breakup that file using the Tokenize function written 
in prog6-1. Once you have the string tokens, you will iterate through all of the string tokens and produce the appropriate token 
object for each string in the list of lists. From this point you will print to the terminal the GetElementType() for each of the 
objects created per line.
