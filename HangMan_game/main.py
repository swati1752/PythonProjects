import random as r
from stages import stages,logo
# HANGMAN

mov = ["raaz", "ajooba", "triangle"] 
print(logo)

print("\nHello, Welcome to Python developed game THE HANGMAN\nYou have to guess the movie which will be choosen raandomly.")

# choosing a random word
movc = r.choice(mov)

# displaying the dashes
print("\nA movie is randomly choosen.")
i=0
st = []
for i in range (0 , len(movc)):
  st += '_'
  i=i+1
print(f"{' '.join(st)}\n")
end_game = False
life = 6

while not end_game:
  guess = input("Guess a letter: ").lower()
  position = len(movc)-1
  for position in range(0,len(movc)):
    if movc[position]==guess:
      st[position] = guess
      #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(st)}")

  if guess not in movc:
    life -= 1
    print(stages [life])
    print("Oops! Wrong Guess.Lost one Life")
    if life == 0:
      end_game = True
      print("You Lose.")
  
  if '_' not in st:
    end_game = True
    print(f"You guessed it Right!\nMovie name is {movc}\nYou Won!")
  
  print(f"life left : {life} \n")