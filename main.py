import os
from math import factorial
from itertools import permutations


def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def getFileName():
    salir = False
    fileWithWords = ''
    while not salir:
        borrarPantalla()
        print("-> Santiago S.R.  (santi72alc@gmail.com) <-")
        print("*** Words permutation ***\n".upper())
        fileWithWords = input("Filename with words to load ? ")

        if fileWithWords == '' or os.path.isfile(fileWithWords):
            salir = True
        else:
            print("The file ["+ fileWithWords + "] NO EXISTS. Please, check!!")
            input("Press 'Enter', please ")
    
    return fileWithWords

def main():
    
    # info()  ---> Falta sacar info de como debe ser el fichero con las palabras
    fileName = getFileName()
    if  fileName == '':
        print("Thanks for using my program!! Bye")
        exit(0)

    print("Loading words from file [" + fileName + "]...")
    arrWords = []
    with open(fileName) as file:
        arrWords = file.readline().rstrip("\n").split(' ')
    print("Loaded!")

    finalPermutations = permuteWords(arrWords)
    
    showResults(finalPermutations)
    
    print("\n*** End !! ***")



def permuteWords(arrWordsToPermute):
    wordsToPermute = []
    arrWordsBlocked = []
    totError = 0

    # For each word in array search and separate blocked words
    for word in arrWordsToPermute:
        if len(word) > 3:
            if word[0:1] == '*':        # Word blocked
                arrWordsBlocked.append(word[1:])
            else:
                wordsToPermute.append(word)
                arrWordsBlocked.append('')
        else:
            totError += 1 

    print("\nTotal Words\t: ", len(arrWordsToPermute))
    print("Blocked\t\t: ", len(arrWordsToPermute)-len(wordsToPermute)-totError)
    print("To permute \t: ", len(wordsToPermute))
    if totError > 0:
        print("Found {} wrong words".format(totError))

    totPermutations = factorial(len(wordsToPermute))
    if totPermutations > 700:
        print("\n*** With this info, will be {} permutacions!!".format(totPermutations))
        resp = input("Are you sure (y/N) ? ").lower()
        if  resp == 's' or resp == 'y':
            print("\n*** Calculating permutations... be patient, please!")
        else:
            print("Aborting!!, See you soon")
            exit(0)

    arrFinal = []
    for permutation in permutations(wordsToPermute):
        i = 0
        tmpArray = []
        for word in arrWordsBlocked:
            if word== '':
                tmpArray.append(permutation[i])
                i += 1
            else:
                tmpArray.append(word)
        arrFinal.append(tmpArray)

    print("\n*** Calculated {} permutations with {} words permuted. Thanks for your waiting!".format(totPermutations, len(wordsToPermute)))
    return arrFinal



def showResults(finalArray):
    row = 1
    for combination in finalArray:
        print("\n#{:02d}".format(row), end='-> ')
        for word in combination:
            print("{}".format(word), end=" ")
        row += 1






## MAIN function
if __name__ == '__main__':
    main()