import random

print("'''~~~~~~~~~~~WELCOME TO RPS GAME~~~~~~~~~~~~'''\n")
        
rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)

    '''

paper = '''

        ___
    ---'___)____
          ______)
          _______)
          ______)
    ---.______)

    '''

scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
           (____)
    ---.__(___)

    '''

game_image = [rock,paper,scissors]

while True:

    user_choice = int(input("Enter your choice: Type 0 for rock, 1 for paper, 2 for secissors: "))

    if user_choice >= 3 or user_choice < 0:
        print("you enterd invalid number, you lose.")
        
    else:
        print(game_image[user_choice])
        computer_choice = random.randint(0,2)
        print("computer chose:")
        print(game_image[computer_choice])
        
        if computer_choice == user_choice:
            print("it's a draw.")
        elif computer_choice == 0 and computer_choice == 2:
            print("you loss")
        elif user_choice == 0 and computer_choice == 2:
            print("you win")
        elif computer_choice > user_choice:
            print("you lose.")
        elif user_choice > computer_choice:
            print("you win")

        repeat = input("do you want to play again? ")
        if repeat == "No" or repeat == "No":
           break

print("Game Over! ")
print(" 'THANK YOU FOR PLAYING' ")

       
        

      





















