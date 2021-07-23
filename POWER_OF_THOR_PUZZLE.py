import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position

def equal_diff(light_x, light_y, initial_tx, initial_ty):
    if light_x > initial_tx :
        if light_y > initial_ty:
            for i in range(abs(light_x-initial_tx)):
                print("SE")
        else: 
            for i in range(abs(light_x-initial_tx)):
                print("NE")
    if light_x < initial_tx :
        if light_y < initial_ty:
            for i in range(abs(light_x-initial_tx)):
                print("SW")
        else: 
            for i in range(abs(light_x-initial_tx)):
                print("NW")

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    if abs(light_x-initial_tx) == abs(light_y-initial_ty):
        equal_diff(light_x, light_y, initial_tx, initial_ty)


    if light_x > initial_tx:
        #print("should increment-->go east")
        increment_x = light_x - initial_tx
        for i in range(increment_x):
            print("E")
            initial_tx = initial_tx+1
            if abs(light_x-initial_tx) == abs(light_y-initial_ty):
                equal_diff(light_x, light_y, initial_tx, initial_ty)

    else: 
        if light_x < initial_tx:
            decrement_x = initial_tx-light_x
            for i in range(decrement_x):
                print("W")
            initial_tx = initial_tx-1
            if abs(light_x-initial_tx) == abs(light_y-initial_ty):
                equal_diff(light_x, light_y, initial_tx, initial_ty)
            #print("should decrement --> go west")
            #
        #else:
            #print("do not move")

    if light_y > initial_ty:
        #print("should increment-->go south")
        increment_y = light_y - initial_ty
        for i in range(increment_y):
            print("S")
            initial_ty = initial_ty+1
            if abs(light_x-initial_tx) == abs(light_y-initial_ty):
                equal_diff(light_x, light_y, initial_tx, initial_ty)
    else:
        if light_y < initial_ty: 
            #print("should decrement --> go north")
            decrement_y = initial_ty-light_y
            for i in range(decrement_y):
                print("N")
                initial_ty = initial_ty-1
                if abs(light_x-initial_tx) == abs(light_y-initial_ty):
                    equal_diff(light_x, light_y, initial_tx, initial_ty)
        #else:
            #print("do not move")
