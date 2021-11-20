import random

# Stone Paper Scissors
def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer chose s
    elif comp == 's':
        if you=='sr':
            return False
        elif you=='p':
            return True
    
    # Check for all possibilities when computer chose w
    elif comp == 'p':
        if you=='s':
            return False
        elif you=='sr':
            return True
    
    # Check for all possibilities when computer chose g
    elif comp == 'sr':
        if you=='p':
            return False
        elif you=='s':
            return True

print("Comp Turn: Stone(s) Paper(p) or Scissor(sr)?")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 'sr'

you = input("Your Turn: Stone(s) Paper(p) or Scissor(sr)?")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")
