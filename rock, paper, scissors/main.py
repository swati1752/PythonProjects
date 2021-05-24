import random


# 0 for rock 1 for paper 2 for sissior
# game
img_list = [ """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""" , 
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]
list = ["rock" , "paper" , "sissior"]
i=random.randint(0,2)
j=random.randint(0,2)

print(f"You choose {list[i]}\n")
print(img_list[i])
print(f"\ncomputer choose {list[j]}\n")
print(img_list[j])

if i==j:
 print("Draw")
elif i==0 and j==2:
  print("You WON!")
elif i>j:
  print("You WON!")
else:
  print("You Lose")
