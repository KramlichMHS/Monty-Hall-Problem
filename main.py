import random
from replit import clear

doorModel = " __\n|  |\n| .|\n|__|\n #"
doorModelBad = " __\n|XX|\n|XX|\n|XX|\n #"
doorModelGood = " __\n|WI|\n|NN|\n|ER|\n #"
doors = [[0,0,0],
         [0,0,0], 
         [0,0,0]]
choosen = False
choice = -1

def randomDoor():
  global doors
  num = random.randint(0,len(doors) - 1)
  doors[num][0] = 1

def printDoors():
  for i in range(len(doors)):
    if doors[i][2] == 0:
      if doors[i][1] == 1:
        print(doorModel + str(i + 1) + "    < Your Choice")
      else:
        print(doorModel + str(i + 1))
    else:
      if doors[i][0] == 0 and doors[i][1] == 0:
        print(doorModelBad + str(i + 1))
      elif doors[i][0] == 0 and doors[i][1] == 1:
        print(doorModelBad + str(i + 1) + "    < Your Choice")
      elif doors[i][0] == 1 and doors[i][1] == 1:
        print(doorModelGood + str(i + 1) + "    < Your Choice")
      else:
        print(doorModelGood + str(i + 1))
    
  print()

def chooseDoor():
  global choice, doors
  choice = int(input("Which door do you want to choose? "))
  doors[choice - 1][1] = 1

def openOneBad():
  global doors
  input("Press enter to open a remaining incorrect door! ")
  clear()
  while True:
    num = random.randint(0, len(doors) - 1)
    if doors[num][0] == 0 and doors[num][1] == 0:
      doors[num][2] = 1
      break
  printDoors()

def swapDoors():
  global choice, doors
  swap = input("Would you like to swap doors? (Yes or No) ")
  if swap.strip().lower() == "yes":
    for i in range(len(doors)):
      if doors[i][1] == 0 and doors[i][2] == 0:
        doors[i][1] = 1
      elif doors[i][1] == 1 and doors[i][2] == 0:
        doors[i][1] = 0
  clear()
  printDoors()

def revealAll():
  input("Press enter to open your door! ")
  for i in range(len(doors)):
    if doors[i][2] == 0:
      doors[i][2] = 1
  clear()
  printDoors()
    
def runOne():
  randomDoor()
  printDoors()
  chooseDoor()
  clear()
  printDoors()
  openOneBad()
  swapDoors()
  revealAll()

runOne()
print("Hello")