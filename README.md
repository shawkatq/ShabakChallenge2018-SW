# ShabakChallenge2018-SW

Shabak challenge 2018 - Software & Data Science

## Getting Started

Every year the Shabak launch a set of challenges in various tech areas, which helps them to recruit quality minds.
Usually, they start it with a simple entry challenge and advertise it over the internet, after you solve it, you will get the complete challenges in various courses. 
The challenge URL: https://www.israelneedsu.com

This is my first repo and my first experience in Python.
I actually liked Python, I found it easy and intuitive to develop with.
I hope you enjoy.

### Prerequisites

To run the code you need to install Python in your machine.
You can refer: https://www.python.org/downloads/ 

### Installing and Running

Just download the py file of each challenge and run it.
I'm using VS Code to develop and run the scripts.

### Entry Challenge 
Simply follow the marked coordinates on the map, zoom in on each point, and you will see a building on a shape of an English letter.
The final answer will be: JOINUS

### Courses menu 
After solving the entry challenge, you will get a nice movie about Shabak, and then the list of courses:
1. Embedded Software
2. Signal Processing
3. Hardware
4. Software & Data Science

I'll explain and give the solutions of "Software & Data Science" course.

### Challenge 1 - Find the Code
After carefully reading the instruction, bottom line, you need to download a zip file, which locked with a password that contains only digits.
There are a lot of tools to crack a zip password, download one or code one, or get an open source one and modify it for our needs, as I did.
Here is a small and easy to understand one: https://github.com/dib0/ZipPasswordCrack
download the code (c# code), open it, and modify it to check only digits. 
After you run it, you will get the cracked password: 262626

This will let you unzip the file, now we got "clue.png", "clueTwo.jpg", "something.txt".
The challenge instructions tell us that "something.txt" is a Python code, let's change the file extension and inspect it with VS Code.
It's obvious that the code needs refactoring, after doing that, go ahead and run it on file "clue.png", the result is a newly generated image with a new clue, hard coded text in image: "Binary, Start 10,000 place, Fibonacci"
hummm, let's see, "Binary" it must be related to the 3rd file "clueTwo.jpg", open it in a Binary Viewer like https://www.onlinehexeditor.com/ , "Start 10,000 place", let's go to that place in the binary remember 1byte = 8bit, so we need actually to go to byte 10000/8=1250 which is 4E2 in hex, "Fibonacci", we will look at bytes with offset according to Fibonacci sequence (0,1,1,2,3,5,8,13....) between each other: 

0-4E2=y

1-4E3=o

1-4E4=u

2-4E6=g

3-4E9=o

5-4EE=t

13-4F6=i

21-503=t

The final answer will be: you got it

### Challenge 2 - The Persian
Again, after reading the instruction, we got a new file, it seems like a JSON file. after inspecting it, we can find that the structure is an object of arrays with the names: "0x1","0x2"..."0x9","0xa","0x14"...."0x64","0xc8"...
which in Decimal are: 1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,200,300,400. hmmm, reminds me of something https://en.wikipedia.org/wiki/Gematria , we will need that for later. now let's look at the array members structure, each one consists of "text" and "value", to be accurate, most of them are like that, take another look, you will find some members like in "0x3" that consists of "return". if we search for all that odd members we will get: "return","in","base64","sum","of","values","below","median", ok we know what that mean, but median of which numbers, what is under "value"? but part of them are "?" which means unknown, how should we calculate them?
Ok, we need more information on the "value" number. look at "text", it can be noticed that "u05" is very common, all the Hebrew letters Unicode starts with "u05". so let's start to identify all the Unicode characters in a "text", and remember the Gematria thing, now it's time to use it, each letter is represented with a number, so if we do a quick check on a short "text", we can see the sum of the Gematric values of the Hebrew letters found on each "text" is the "value". now we can find all the missing values, and find the "median" of those values, and then the sum of values below that median converted to base64 as hint told us to do.
see the solution code in Python.

### Challenge 3 - The Usual Suspect
This one is not easy, read the instructions carefully, now we got a big csv file which contains a log of activities of users on the net. and we have a list of users that know as suspects.
You can download the log from: https://drive.google.com/open?id=1mucrMI7Pm_tHKwI3BjOFBVXvQCmdnO9-

First, let's separate the suspects apart from the others and put them in a different two files. ok, now we need to look at the suspects activities, if we sort the file by "userid" and "date", we will see that the suspects have a non-constant number of activities each day, with a concentration of most of the activities in 2-3 days, interesting, so what about examin this behavior on others, simply we will count the activity in each day for each user, and search for the same pattern we noticed for the suspects. this will get us the additional suspects. don't forget that we need there most used IP address.

See the solution code in Python. (be carefull, the IPs needs to be submitted as answer at the same order as the userids in ascending order).

Another approach, we can see that the suspects activities from the most used IP occurred in constant time intervals, we can try and search a similar behavior on the other users. and this should give us the same result (it's a bit messy and not efficient so I didn't add the code for that).

Feel free to give me advices and corrections

Good luck
