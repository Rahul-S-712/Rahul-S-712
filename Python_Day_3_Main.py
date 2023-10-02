print(r'''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
''')
print(r'''
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
''')

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
direction = input("\nYou're at a cross-road. Do you want to go left or right ? Where do you want to go ? Type 'left' or 'right' : ")

if direction == "left" :
  print("\nYou decide to go left. As you walk down the path you reach a lake.")
  print("There is an island in the middle of the lake.")
  print("You can either wait for a boat or swim across the lake to get to the island.")
  swim_or_wait = input("What will you do ?\nType 'wait' to wait or 'swim' to swim across : ")

  if swim_or_wait == "wait" :
    print("\nYou arrive at the island unharmed.")
    print("There is a house with 3 doors. One red, one yellow, and one blue.")
    print("Which do you choose ?")
    door = input("Enter 'red', 'blue', or 'yellow' : ")

    if door == "red" :
      print("\nYou choose to go through the red door.\nAs you walk in through the door, it shuts behind you and locks you in.")
      print("The room then starts to catch fire. You are burned to death.")
      print("G A M E    O V E R")

    elif door == "blue" :
      print("\nYou choose to go through the blue door.\nAs you walk in through the door, it shuts behind you and locks you in.")
      print("A hungry beast emerges from the shadows and leaps onto you. You get mauled to death.")
      print("G A M E    O V E R")

    elif door == "yellow" :
      print("\nYou choose to go through the yellow door.\nAs you walk in through the door, it shuts behind you.")
      print("You find a chest at the corner of the room. You walk towards it and you open it.")
      print("You find a chest full of gold coins. You did it ! You found the treasure !")
      print("\nY O U    W I N")

    else :
      print("\nG A M E    O V E R")
      
  else :
    print("\nYou decide to swim across the lake.")
    print("As you are swimming across, you get attacked and killed by piranhas.")
    print("G A M E    O V E R")
else : 
  print("\nYou step on a booby trap and you fall into a hole in the ground.\nG A M E    O V E R")
