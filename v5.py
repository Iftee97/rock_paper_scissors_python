import random

print("\n---[Rock, Paper, Scissors]---\n")

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

'''
Rock wins against Scissors
Scissors wins against Paper
Paper wins agains Rock
'''

print("\n0 for Rock, 1 for paper, 2 for scissors\n")

choices = [rock, paper, scissors]

user_number = int(input("enter choice: "))
user_choice = choices[user_number]

random_number = random.randint(0, 2)
computer_choice = choices[random_number]


if user_choice == rock and computer_choice == scissors:
    print(
        f"user choice: {user_choice}\ncomputer choice: {computer_choice}\n[user won]")

elif user_choice == scissors and computer_choice == paper:
    print(
        f"user choice: {user_choice}\ncomputer choice: {computer_choice}\n[user won]")

elif user_choice == paper and computer_choice == rock:
    print(
        f"user choice: {user_choice}\ncomputer choice: {computer_choice}\n[user won]")

elif user_choice == computer_choice:
    print(
        f"user choice: {user_choice}\ncomputer choice: {computer_choice}\n[draw]")

else:
    print(
        f"user choice: {user_choice}\ncomputer choice: {computer_choice}\n[computer won]")
