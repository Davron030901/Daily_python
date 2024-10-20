import random
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images=[rock,paper,scissors]
user_choice=int(input('What do you choose ? type 0 for Rock, 1 for paper or 2 for Scissor.'))
computer_choice=random.randint(0,2)
print(game_images[user_choice])
print(f"Computer Chose:\n{game_images[computer_choice]}")
if user_choice>=0 and user_choice<=2:
    if user_choice==computer_choice:
        print("It's a draw")
    elif user_choice==0:
        if computer_choice==1:
            print("You lose")
        else:
            print("You Win!")
    elif user_choice==1:
        if computer_choice == 2:
            print("You lose")
        else:
            print("You Win!")
    else:
        if computer_choice==0:
            print("You lose")
        else:
            print("You Win!")
else:
    print("Chose no correct")
