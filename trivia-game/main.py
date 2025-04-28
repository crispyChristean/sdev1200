#
# Christian Espinoza 
# 2/12/2025
# Trivia Game Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program. 
import random 
from classQuestions import question
from classQuestions import player 

def determineWinner(obj, job):
    if obj.amountCorrect > job.amountCorrect:
        print('Player One has greater Points, Player One WINS!')
    elif obj.amountCorrect < job.amountCorrect:
        print('Player Two has Greater Points! Player Two WINS!')
    else:
        print('BOOO, it is a draw :(') 

questionOne = question(
    "What is 2+2?: ",
    "4",
    "7",
    "9",
    "10",
    "4"
)

questionTwo = question(
    "Who painted the Mona Lisa?: ",
    "Mona Lisa",
    "Joann of Arc",
    "leonardo dicaprio",
    "Da Vinci",
    "Da Vinci"
)

questionThree = question(
    "When was the Declaration of Independence Signed",
    "1767",
    "1776",
    "1655",
    "2005",
    "1776"

)

questionFour = question(
    "What is the Powerhouse of the cell?",
    "Nucleus",
    "Cytoplasm",
    "Mitochondria",
    "Vacuole",
    "Mitochondria"
)


questionFive = question(
    "What was the name of the man who suffered a sever Radiation case in 1999",
    "Akira Howard",
    "Hisashi Ouchi",
    "Gen Asagiri",
    "Yoshihiro Togashi",
    "Hisashi Ouchi"
) 

questionSix = question(
    "what amendment is women's suffrage?",
    "51st",
    "14th",
    "19th",
    "31st",
    "19th"
)

questionSeven = question(
    "What animal is amphibious and can regenerate organs/limbs",
    "Axolotl",
    "bear",
    "Bobcat",
    "Legion",
    "Axolotl"
)

questionEight = question(
    "What Artist drew Women with high defenition muscles in the 16th Century",
    "Da Vinci",
    "Andy Warhol",
    "Michael Angelo",
    "Edgar Allen Poe",
    "Michael Angelo"
)

questionNine = question(
    "Who is the world famous comic book artist that revolutionized action series",
    "Robert Kirkman",
    "Akira Toriyama",
    "William Shakespeare",
    "Hirohiko Araki",
    "Hirohiko Araki"
)

questionTen = question(
    "Who was mainly credited to make the First Nuclear Bomb?",
    "Dwight Eisenhower",
    "albert einstein",
    "Robert Oppenheimer",
    "George Patton",
    "Robert Oppenheimer"
)
playerOne = player()
playerTwo = player()



#Player One game 
allGames = [questionOne, questionTwo, questionThree, questionFour, questionFive]
secondGames = [questionSix, questionSeven, questionEight, questionNine, questionTen]
for iteration in allGames:
    test = iteration.askQuestion()
    test = iteration.check(test)
    if test == True:
        playerOne.addPoint()

print("SECOND PLAYER'S TURN")
for iteration in secondGames:
    test = iteration.askQuestion()
    test = iteration.check(test)
    if test == True:
        playerTwo.addPoint()

print(f'First Players Results: {playerOne.showPoints}\nSecond Players Results')
determineWinner(playerOne, playerTwo)