import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


index=0
# game loop
while True:
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        if i==0:
            largest_height=mountain_h
            
        if  mountain_h >= largest_height:
            largest_height = mountain_h
            #print("largest height is :", largest_height)
            index=i
    
    #print(largest_height)
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # The index of the mountain to fire on.
    #Destroying largest mountain out of 8 in each trial run
    print(index)

