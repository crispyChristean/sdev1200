class question:
#Setting object attributes.
    def __init__(self, trivia, a1, a2, a3, a4, correct):
        self.trivia = trivia
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.correct = correct

    def askQuestion(self):
        print(self.trivia)
        print(f'{self.a1}\n{self.a2}\n{self.a3}\n{self.a4}')
        given = input("What is your answer: ")
        return given

    def check(self, given):
        if given == self.correct:
            given = True
        else:
            given = False 
        return given

class player:
    def __init__(self): 
        self.amountCorrect = 0
    def addPoint(self):
        self.amountCorrect +=1
    def showPoints(self):
        print(self.amountCorrect)