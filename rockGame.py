import random

print("welcome to Rock Paper Scissors GAME.")

userCount = 0
computerCount = 0
tied = 0

def generateComputerChoice():
    li = ["Rock", "Paper", "Scissors"]
    computerChooseg = random.choice(li)
    return computerChooseg

# for i in range(10):
#     print(generateComputerChoice())


def askFromUser():
    is_playing = input("do you again want to play the game\n")
    if is_playing.lower() == 'yes' or is_playing.lower() == 'y':
        playGame()


def printResult(whoWins,userChoose,computerChoose):
    if whoWins == 0:
        print("you choose " + userChoose + " and computerChoose " + computerChoose)
        print("Yahh You WON the game, Here is the updated Score..")
    elif whoWins == 2:
        print("you choose " + userChoose + " and computerChoose " + computerChoose)
        print("You LOST the game, Here is the updated Score..")
    else:
        print("you choose " + userChoose + " and computerChoose " + computerChoose)
        print("GAME TIED")


def showScore(userCount, computerCount, tied):
    print("YourScore: ", userCount)
    print("ComputerScore ", computerCount)
    print("tied", tied)


def playGame():
    whoWins = -1
    global userCount
    global computerCount
    global tied
    computerChoose = generateComputerChoice()
    userChoose = input("choose one of these from Rock Paper Scissors\n")
    if userChoose.lower() == "rock" and computerChoose.lower() == "scissors":
        userCount = userCount + 1
        whoWins = 0
    elif userChoose.lower() == "paper" and computerChoose.lower() == "rock":
        userCount = userCount + 1
        whoWins = 0
    elif userChoose.lower() == "scissors" and computerChoose.lower() == "paper":
        userCount = userCount + 1
        whoWins = 0
    elif userChoose.lower() == computerChoose.lower():
        tied = tied + 1
        whoWins = 1
    else:
        computerCount = computerCount + 1
        whoWins = 2

    printResult(whoWins,userChoose,computerChoose)
    showScore(userCount,computerCount,tied)
    askFromUser()


playGame()


