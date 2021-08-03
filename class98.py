
def filePath():
    file = input("Tell the Locationof the File: ")
    wordNo = 0
    openFile = open(file, "r")
    for line in openFile:
        word = line.split()
        wordNo = wordNo + len(word)
    print(wordNo)

filePath()
