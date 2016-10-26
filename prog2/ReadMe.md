1) In this assignment you will play the role of Cheaty McCheaterpants. Your instructor, BigBritches McMakesyouwork, 
has just assigned you your final project for the semester. After checking your grade (and spending more time doing 
math to figure out the minimum score you need to pass than you did studying the entire semester) you have come to the 
conclusion that with a score of 100% you are going to receive exactly 70% in the class, any less and you will fail (mostly 
because you think extra credit is for suckers). Unfortunately for you, Cheaty McCheaterpants, you don't even know how to 
start the actual assignment. Fortunately you know the finer points of success; cheating, lying and stealing. You also have me, 
your helpful narrator. The following three steps will lead us to an illegitimate C in this god forsaken course.

  a. Step 1. We know that you need a perfect score on the final project, and we know from the way some of the less socially aware 
students brag that they are getting 100% on every assignment AND that they are already done with the assignment. Unfortunately,
because you don't associate with people like that, you have no idea what their name is or, more importantly, their login information. 
We do, however, know three very important pieces of information.

    i. McMakesyouwork is lazy about his account security. 
    ii. He has a gradebook in his account.
    iii. He keeps the student login information in his account.
    iv. Gradebook:
                /home/ma/j/lindenea/ClassInfo/Grades
    v. Login Information:
                /home/ma/j/lindenea/ClassInfo/Logins
                

Write a script that takes two arguments. The first argument should be the grades file location and the second argument should be the 
logins file location. Your script must determine the name of the student that has received 100 on all of the assignments and echo that 
name to stdout. Next your script must determine both the login name and password for that user and echo that information as well.
<NAME>
<USERNAME>
<PASSWORD>



  b. Step 2. Try logging into the account! Whats that? Smarty McBetterthanyou changed their default password??? That Jerk! Fortunately, 
Smarty didn't change their account security settings and we can just navigate directly to their account (use the username you found 
in step 1):  /home/ma/237.01/<USERNAME>/

Unfortunately their account is a mess. They have files everywhere with nonsense names and no file extensions! We do know something 
about the class fortunately. We know that all of the assignments are written in C! Write a script that takes a single argument. The 
argument will be the root directory from which it will open all of the files in every folder in the supplied home folder and then copies
all of the C programs to the current directory (the directory the script is run from) and make sure you tack a “.c” onto the end of 
each of those files. Every time a file is copied, it should echo the final name of the file copied (including the “.c”). (There are 
four files you want). Use this on Smarty's home directory to copy all of his C programs!
<File 1>
<File 2>
<File 3>
<File 4>


  c. Step 3. Now that you have all of Smarty's C programs we have to figure out which one is the final project. We literally don't 
  care enough to figure out what the final project is supposed to do, but we do know what the first three assignments did.

    i. Assignment #1 Took in a single integer in degrees and printed out the cosine of the input to three decimal places.
    ii. Assignment #2 Took in a single integer and printed out the square root of the input to four decimal places.
    iii. Assignment #3 Took in a single integer and printed out that number divided by 10 to five decimal places.
    
Based on this information write a script that takes four command line arguments compiles each of the c programs that matches 
one of those command line arguments, determines which assignment each one is and echos the file name and the assignment that it 
corresponds with. Use this script to determine which .c file goes with each assignment.
<File 1> <Assignment #>
<File 2> <Assignment #>
<File 3> <Assignment #>
<File 4> <Assignment #>
