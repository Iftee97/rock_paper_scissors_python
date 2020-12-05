import random

rock = '''
rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to Rock, Paper, Scissors Game\n")
print("Rock beats Scissors")
print("Paper beats Rock")
print("Scissors beat Paper\n")
print("player makes the first move, then the computer makes it's move at random")
rps = [rock, paper, scissors]

player_number = int(input("""\n0 for Rock, 
1 for Paper, 
2 for Scissors\n\n
Enter Number: """))

player_choice = rps[player_number]
print(f"\nplayer chose: {player_choice}")

computer_number = random.randint(0, 2)
computer_choice = rps[computer_number]
print(f"\ncomputer chose: {computer_choice}")

# 0 -> rock
# 1 -> paper
# 2 -> scissors

if player_number == computer_number:
    print("Draw")

elif player_number == 0 and computer_number == 1:
    print("Computer Won!")

elif player_number == 0 and computer_number == 2:
    print("Player Won!")

elif player_number == 1 and computer_number == 0:
    print("Player Won!")

elif player_number == 1 and computer_number == 2:
    print("Computer Won!")

elif player_number == 2 and computer_number == 0:
    print("Computer Won!")

elif player_number == 2 and computer_number == 1:
    print("Player Won!")