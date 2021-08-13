# CSC 59005 Coding Challenge 1 Solution

### Question 1:

Write a program to replace all taboo words, saved in taboo file, in all .txt files in the current directory with the corresponding number of ‘\*’, e.g. if there are 2 words in taboo: ‘bad’ and ‘worse’, then any word ‘bad’ and ‘worse’ in a txt file will be replaced by ‘\*\*\*’ and ‘\*\*\*\*\*’, and your program output the number of such replacements after processing each file, if there are more than 5 taboo words in a file, the file is moved to the ‘trash’ folder.

## Solution Method:

The only real work needed to be done is to figure out how to get a list of all .txt files in the current directory and how to move the file to the 'Trash' / 'Recycling Bin'. For getting the list of .txt files in the current directory, we can use Python's os package to list all entries in the current directory and then from that list, we can filter out the entries that end with ".txt". For sending the file to the trash if it has more than 5 taboo words, we can use an external package send2trash (installed using **_pip install Send2Trash_**) that natively sends files to the 'Trash' / 'Recycling Bin'. Replacing the taboo words in a file is simple due to Python's built-in string operations. However we can use Python's re package for regex to also remove taboo words with case insensitivity and count the number of entries that matched the regex pattern.

### Taboo List:

The file **_taboo.txt_** holds the list of taboo words, in which it's formatted such that there's one taboo word per line.

![alt text](https://github.com/cyanChill/CSC-59005-Code-Challenge-1/blob/main/images/Taboo%20File.PNG "taboo.txt")

### Sample Inputs:

These are the 3 text files we'll be using our program on:

![alt text](https://github.com/cyanChill/CSC-59005-Code-Challenge-1/blob/main/images/Sample%20Input%201.PNG "Sample Input 1")
![alt text](https://github.com/cyanChill/CSC-59005-Code-Challenge-1/blob/main/images/Sample%20Input%202.PNG "Sample Input 2")
![alt text](https://github.com/cyanChill/CSC-59005-Code-Challenge-1/blob/main/images/Sample%20Input%203.PNG "Sample Input 3")

After running our program, the files will look like this:

![alt text](https://github.com/cyanChill/CSC-59005-Code-Challenge-1/blob/main/images/Sample%20Output%201.PNG "Sample Output 1")
![alt text](https://github.com/cyanChill/CSC-59005-Code-Challenge-1/blob/main/images/Sample%20Output%202.PNG "Sample Output 2")

![alt text](https://github.com/cyanChill/CSC-59005-Code-Challenge-1/blob/main/images/Sample%20Output%203a.PNG "Sample Output 3a")
![alt text](https://github.com/cyanChill/CSC-59005-Code-Challenge-1/blob/main/images/Sample%20Output%203b.PNG "Sample Output 3b")

> Note: The first image for file3.txt shows that the file has been deleted due to it having more than 5 taboo words. The second image for file3.txt shows that the file that was deleted had its taboo words replaced with the appropriate amount of '\*'.

The console output to the program looks like this:

![alt text](https://github.com/cyanChill/CSC-59005-Code-Challenge-1/blob/main/images/Console%20Output.PNG "Console Output")

> > > > > > > code-challenge-1/main
