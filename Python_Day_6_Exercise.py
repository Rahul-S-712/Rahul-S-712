# 100 Days of Code - Python
# Day 6
# Date :- 07/10/2023

# Go to link : 
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

# Then Paste Code in the designated section and run

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    if (wall_in_front() == True):
        turn_left()
        move()
        turn_right()
    if (front_is_clear() == True):
        move()
        turn_right()
        while (front_is_clear() == True):
            move()
        turn_left()

while (at_goal() != True):
    if (front_is_clear() == True):
        move()
    elif (wall_in_front() == True):
        jump()
