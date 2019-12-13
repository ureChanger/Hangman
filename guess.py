class Guess:

    def __init__(self, word):
        self.secretWord = str(word)
        self.currentStatus = "_"*len(word)
        self.guessedChars = []
        self.numTries = 0


    def display(self):
        print("현재까지 맞춘 글자 : %s\n살패한 회수 : %d"%(self.currentStatus,self.numTries))
        pass


    def guess(self, character):
        if(character in self.secretWord):
            currentChangeStr=""
            strCheckIndexList = []

            #self.secretWord 의 어떤 인덱스에 character가 있는지 확인
            for i in range(len(self.secretWord)):
                if self.secretWord[i] == character :
                    strCheckIndexList.append(i)

            #self.currentStatus 바꾸어주기
            for i in range(len(self.currentStatus)) :
                if self.currentStatus[i] != "_":
                    currentChangeStr += self.currentStatus[i]

                else:
                    if i in strCheckIndexList :
                        currentChangeStr += character
                    else:
                        currentChangeStr += "_"

            self.currentStatus = currentChangeStr
            self.guessedChars.append(character)

        else :
            self.numTries += 1

        if self.currentStatus == self.secretWord :
            return True

        return False