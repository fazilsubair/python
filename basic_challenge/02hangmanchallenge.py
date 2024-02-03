# create a greeting 
# create your wordlist 
# randomly choose a word from the wordlist
# ask the user to guess a letter
# bonus make the program take input from the user and make it lowercase
# check the letters is in word
import random
print("hello user. welcome to hangman ")

def wordlistFunciton():
    wordlist = [ ]
    wordListCount = int(input("how many words would you like to enter: "))
    print("enter the words")
    for i in range(0,wordListCount):
        wordlist += [input()]
    # print(wordlist)
    return wordlist

def letterCheck(guessedLetter,randomword):
    if guessedLetter in randomword:
        print(f"the letter {guessedLetter} is present in {randomword}")
    else:
        print(f"the letter {guessedLetter} is not present in {randomword}")
    


wordList = wordlistFunciton()
randomword  = random.choice(wordList)
guessedLetter = input("enter a letter from A-Z: ").lower()
letterCheck(guessedLetter,randomword)
