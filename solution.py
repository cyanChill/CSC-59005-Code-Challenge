import re           # Used for regex operations
import os           # Used to list files in directory
import shutil       # Used to move files from one directory to another
import send2trash   # Module that sends files to 'Trash' / 'Recycling Bin'

def replace_taboo(txtfile: str, taboolist: list[str]):
    '''
    Replace all taboo words with * and returns the number of replacements 
    (cnt) and if cnt > 5, moves the file to 'Trash' / 'Recycling Bin'.

        Parameters:
            txtfile (str): A string representing the name of a text file
            taboolist (list[str]): A list containing taboo words

        Returns:
            cnt (int): Total number of replacments of taboo words in text 
                       file
    '''
    if not taboolist:
        return 0
    
    try:                            # Make sure 'txtfile' is a text file
        f = open(txtfile, "r+")
    except FileNotFoundError:
        return 0

    cnt = 0
    fcontents = f.read()
    f.seek(0)

    for tabooword in taboolist:
        # Create a pattern to look for the taboo words with case insensitivity
        p = re.compile(tabooword, re.IGNORECASE)
        cnt += len(p.findall(fcontents))
        # Replace all occurrences of the taboo words (case insensitive)
        # with the appropriate amount of "*"
        fcontents = p.sub("*"*len(tabooword), fcontents)
    
    f.write(fcontents)
    f.close()

    if cnt > 5:
        # Send file to 'Trash' / 'Recycling Bin':
        send2trash.send2trash(txtfile)

        # If put in 'trash' folder in current directory:
        #try: 
        #   os.mkdir("./Trash")
        #except:
        #  pass
        # Move the current file to 'trash' folder in current directory
        #shutil.move("./" + txtfile, "./Trash")
    return cnt

def find_replace_taboo(taboofile: str):
    '''
    Gets a list of taboo words from a file and then replaces all taboo
    words in all .txt files in the current directory with the 
    corresponding number of '*' and prints the number of replacements
    (excludes the file holding the list of taboo words)

        Parameters:
            taboofile (str): A string representing the name of the file
                             holding the taboo words
    '''
    try:                           
        with open(taboofile, "r") as t:
        # Get a list of taboo words and put it in a list (automatically 
        # removes extra whitespaces) from "taboo.txt" which is formatted 
        # with 1 taboo word per line 
            taboolist = [x.strip() for x in t.readlines() if x.strip()]
    except FileNotFoundError:
        return None

    # Get a list of all text files in the current directory
    txtfilelist = [f for f in os.listdir() if f.endswith(".txt")]

    for txt in txtfilelist:
        if txt != taboofile:
            numreplace = replace_taboo(txt, taboolist)
            print("There were", numreplace, "replacements in", txt)


# Testing Code
find_replace_taboo("taboo.txt")
