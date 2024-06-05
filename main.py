import os
def wipescreen():
    os.system("cls")

def printlettercount(letter,string):
    count = 0
    for i in string:
        if i == letter:
            count += 1
    return count

def countwords(file):
    words = file.split()
    return len(words)

def main():
    file = "books/frankenstein_novel.txt"
    with open(file) as f:
        file_contents = f.read()
    file_contents = file_contents.lower()

    while True:
        wipescreen()
        selection = input("(1) Count words\n(2) Count letter\n(3) Exit\nEnter: ")
        if int(selection) == 1:
            wipescreen()
            print(f"There are {countwords(file_contents)} words in this book")
            input("Enter to continue")
        elif int(selection) == 2:
            wipescreen()
            lettertest = input("Which letter are we testing: ")
            wipescreen()
            print(f"There are {printlettercount(lettertest,file_contents)} instances of {lettertest} in this book")
            input("Enter to continue")
        else:
            break

wipescreen()
main()