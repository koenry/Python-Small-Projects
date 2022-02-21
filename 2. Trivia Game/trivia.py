import logging
import json
import random

def trivia():
    print('Welcome to the super awesome amazing \n QUIZ GAME!!! \n (type in "exit" to exit the game!) \n')
    with open('./jsons/trivia.json') as f:

        dataTrivia = json.load(f)
        answers = ['A', 'B', 'C', 'D']
        i = 0
        score = 0
        while True:
            randNum = random.randrange(1, 541)
            print('\n')
            print(dataTrivia[randNum]['question'])
            while i < 4:
                answers2 = dataTrivia[randNum][answers[i]]
                print(answers[i] + '. ' + answers2)
                i += 1

            i = 0
            choice = input('Enter your answer A-D: ').upper()

            # lets stop the pesky users from entering something different and their score dropping down for it
            while not choice in answers:
                if choice == 'EXIT':
                    break  # we break out of this loop
                else:
                    choice = input(
                        'PLEASE ENTER ONLY: "A B C D" !!!!\n').upper()
            if choice == 'EXIT':
                break  # we stop the game

            elif choice == dataTrivia[randNum]['answer']:
                print('\n CORRECT!!! \n ')
                score += 1
                print('Score: ' + str(score))
            else:
                print('\n WRONG!!! \n ')
                score -= 1
                print('Score: ' + str(score))
                print('\n'+'Correct Answer:' +
                      dataTrivia[randNum]['answer'])
                if score < -9:
                    print('\n YOU LOST !!!!!')
                    break
trivia()

