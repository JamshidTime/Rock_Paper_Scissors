import random
from pickle import encode_long

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

Game_Images = [rock, paper, scissors]

User_Choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
)
if User_Choice >= 0 and User_Choice <= 2:
    print(Game_Images[User_Choice])

Computer_Choice = random.randint(0, 2)
print("Computer Chose:")
print(Game_Images[Computer_Choice])

if User_Choice >= 3 or User_Choice < 0:
    print("You typed an invalid number. You lose!")
elif User_Choice == 0 and Computer_Choice == 2:
    print("You Win!")
elif Computer_Choice == 0 and User_Choice == 2:
    print("You lose!")
elif Computer_Choice > User_Choice:
    print("You lose!")
elif User_Choice > Computer_Choice:
    print("You win!")
elif Computer_Choice == User_Choice:
    print("It's a draw!")
