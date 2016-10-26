In this assignment you have been hired by a mid size corporation to perform some corporate espionage. Your target is a set of encrypted 
documents. In this project you will obtain, break and decode these documents for your employer.

  Your employer, Silly Parts Inc, know that an employee for their rival company, Terrible Tribbles, is also in your class. The Terrible 
  Tribbles employee, Yoko Jamika, is known to you and you know that they do not have very good security practices. It is probable that 
  they use the same password on a number of accounts. If you could find their password for the class you should be able to login to their 
  named account on the Terrible Tribbles san diego server. After you log into the server you should be able to find a set of encrypted 
  files, and the encryption executable in their directory
  
    For this first step, you will need to write a script that takes three arguments. The first argument will be a password file (You 
    do know where to obtain this information right? You found them in the last assignment). The second argument will be a target server, 
    for this assignment the Terrible Tribbles server is hosted at: sd.lindeneau.com . The third argument will be a user name, you know 
    that in companies it is common to use an employee's first name as their user name (among other combinations, but for this assignment
    we are using the first name).This script will obtain Yoko's password from the provided source (argument 1). It will then copy all 
    of the files in Yoko's home directory on the target server (argument 2) with the .enc extension, in addition to the encryption 
    executable: encryptor to your current directory. You are encouraged to use the scp program, which will allow you to securely copy 
    files from a remote server to your current local directory. An example of copying the remote encryptor executable to the current 
    directory is:
         expect -c "
             spawn scp <USERNAME>@<TARGET>:encryptor .
             expect password: { send <PASSWORD>\r }
             sleep 1
             exit "




The second part of this assignment will be to figure out how to break the encryption. Fortunately for us, Yoko's encryption program 
is custom made and is based upon one of the oldest, and most broken, encryption schemes: the Caesar Cipher. We don't have any cleartext 
files, but we do have the encryptor executable, which has the key embedded into the executable. To get ahold of some cleartext we can 
simply generate some known plaintext (we just pick some text... literally anything you want) and then pass it into the encryptor 
executable on standard in. The encryptor program will output the encrypted text on standard out. To break the encryption, we need to 
figure out the offset between the plaintext and the resulting ciphertext.
To accomplish this you will need to write a c program and a script. The c program will calculate the offset used in the encryptor 
program and the script will automate the process.

The c program will take a command line argument and a phrase on standard in. The command line argument will be the plaintext and the 
standard input will be the ciphertext. Your program prog3-2.c should then output the difference between between the characters that 
are passed on the command line and the characters that are input through standard input. (The minimum number of characters you will 
need to figure this out is 1. Yes 1. You only need to have 1 character where you know both the plain and cypher text to break a Caesar 
Cipher). An example of a call to this program is: echo “k” | ./prog3-2 g




The third part of this program will also consist of both a c program and a script. The purpose of this section is to decipher the 
encrypted files you obtained in part 1. The c program will implement the Caesar Cipher. There are number of resources on how to do 
this online. Your program should take a command line argument, which will be the offset, while the input through standard in will 
be the part that will be rotated(encrypted/decrypted). To simplify this assignment you will only need to rotate characters that are 
alpha characters (letters). No other characters should be rotated. You can also assume that the input will only be a single line long.

Your script will take a single command line argument, which will be the rotation argument to the Caesar c program you wrote above. 
Your script should then call the prog3-3 you wrote above on each of the .enc files you got in step 1. Your script should output 
a .dec file for each .enc file that exists. It should echo the name of each .dec file it generates. (You will be able to use the 
negative of the number you found in step 2. This is how you decrypt Caesar Cipher encryptions.)

