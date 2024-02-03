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

def letterCheck(guessedLetter,randomword,dummylist):

    for i in range(len(randomword)):
        letter = randomword[i]
        if letter == guessedLetter:
            dummylist[i] = letter

    
    return dummylist


    #     print(f"the letter {guessedLetter} is present in {randomword}")
    # else:
    #     print(f"the letter {guessedLetter} is not present in {randomword}")
    

dummylist = []

wordList = wordlistFunciton()
randomword  = random.choice(wordList)

for i in randomword:
    dummylist += "_"

print(dummylist)
gameover =False
while not gameover:
    guessedLetter = input("guess a letter : ").lower()
    dummylist = letterCheck(guessedLetter,randomword,dummylist)
    print(dummylist)
    if "_" not in dummylist:
        gameover = True
        print("congrats you have won!!!!")
