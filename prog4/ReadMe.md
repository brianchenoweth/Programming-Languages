There has been a recent surge in applicants to your software engineering firm. Your boss has recently instated a simple programming 
test to weed out the applicants who can’t program. Your job is to automate the task of running the submitted programming tests. To 
accomplish this you know that you can write a shell script that will take the applicants file as a command line argument and a 
‘Correct’ output file as another command line argument and compare the output from the applicants program with the correct output. 
Unfortunately for you all of the submitted programs are written in Lua and your boss won’t let you install Lua on your server. To 
get around this you know that you can write your own Lua execution environment in C. The final step will be to write some Lua code 
to verify that the whole setup is working.

First, we must be able to execute some Lua code. To do this we are going to build a basic Lua interpreter. We know that we do not 
have to have a full-fledged interpreter, and that it only has to tell the lua environment to do the file that we will have passed as 
the first command line argument after the environment has been setup. Something along the lines of a very basic environment as 
described in the lua documentation1 should do it. Probably wont need anything loopy and a single luaL_dofile2 call will be sufficient.

To get this bad boy to compile there are going to be a total of four(4) new compiler flags and one old one. It is ugly, long and 
complicated. I will try to explain what is going on after:
gcc <FILE.C> -llua -lm -L /home/ma/j/lindenea/lua/lib/ -I /home/ma/j/lindenea/lua/headers/ -R /home/ma/j/lindenea/lua/lib
This should all be on one line, but it doesn’t fit. Basically it looks like this:
     gcc <FILE.C>  -llua -lm -L <LDIR> -I <HDIR> -R <SODIR>


The <FILE.C> is the file we want to compile. The -L <LDIR> bit tells the compiler where to find the compiled library files such that 
the linker can find the symbols and use the right memory addresses for them. The -llua portion tells the linker to do this. The 
-lm portion tells it to link to the default math library. The -I <HDIR> portion tells the compiler where to find those fancy headers 
we found/used in the reference manual. The -R <SODIR> bit tells the compiler to add some extra fancy flags to our executable. These 
flags tell the executable where to find non- default (not installed) dynamically linked libraries (.so on *nix & .dll on windows). 
This is one of those nifty flags that allows us to ship programs that rely on specific libraries that might not be installed on a 
target system as long as we bring our own version of the library with our executable code.


Second, we are going to need a simple lua program to test our C code. This Lua file should be the test that your boss has set out 
for your applicants. What was that test? Oh, right. FizzBuzz from 1 to 100.


Third, we are going to write a shell script that will compile our C code and then execute the file passed as the first command 
line argument. If the output from the code does not match the contents of the file that is passed as the second argument then your 
script should print “Failed Test” otherwise it should print “Passed Test”.
