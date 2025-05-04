import random
def generateComputerMove():
    game_list = ["rock", "paper", "scissors"]
    computer_input = game_list[random.randrange(0, 3)]
    return computer_input

def takeHumanInput():
    while True:
        human_input = input("Choose from rock, paper or scissors: ")
        if(human_input == "rock" or human_input == "paper" or human_input == "scissors"):
            return human_input.lower()

def determineWinner(rounds):
    human_count = 0
    computer_count = 0
    for i in range(0, rounds):

        computer_input = generateComputerMove()
        human_input = takeHumanInput()

        if(human_input == computer_input):
            human_count += 1
            computer_count += 1
            print("Computer Input: "+str(computer_input)+"\nDraw!")
        elif((human_input == "rock" and computer_input == "paper") or (human_input == "paper" and computer_input == "scissors") or (human_input == "scissors" and computer_input == "rock")):
            computer_count_count += 1
            print("Computer Input: "+str(computer_input)+"\nComputer Won!")
        else:
            human_count += 1
            print("Computer Input: "+str(computer_input)+"\nHuman Won!")

        if(human_count == computer_count):
            continue
        elif(human_count>(rounds/2)):
            print("Human won the GAME!\nRounds Won: "+str(human_count)+"/"+str(rounds))
            break
        elif(computer_count>(rounds/2)):
            print("Computer won the GAME!\nRounds Won: "+str(computer_count)+"/"+str(rounds))
            break

def main():
    try:
        while True:
            rounds = int(input("How many rounds do you want to play (odd number): "))
            if (rounds %  2 != 0):
                break

    except Exception as e:
        print(e)
    determineWinner(int(rounds))

if __name__ == "__main__":
    main()