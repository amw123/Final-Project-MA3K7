import numpy as np
import random

def choose_fullest(arr):
    arr = np.asarray(arr)

    max_v = np.max(arr) # largest volume
    max_positions = np.where(arr == max_v)[0] #location of fullest glass(es)

    # Look at glasses adjacent to fullest
    adjacent_g = np.zeros(len(max_positions)*2)

    for i in range(len(max_positions)):

        adjacent_g[2*i] = arr[(max_positions[i] - 1)%len(arr)] #left
        adjacent_g[2*i+1] = arr[(max_positions[i] + 1)%len(arr)] #right

    #Find max with best adjacent value
    best_max = np.where(adjacent_g == max(adjacent_g))[0][0]//2
    best_max = max_positions[best_max]
    side = np.where(adjacent_g == max(adjacent_g))[0][0]%2
    if side == 0: #left
      best_adjacent = (best_max -1)%len(arr)
      return int(best_adjacent), int(best_max)
    else: #right
      best_adjacent = (best_max +1)%len(arr)
      return int(best_max),int(best_adjacent)


n= 4
glasses = np.zeros(4)
overflow =  False
round =0

# We play as Ali
# Beth is the robot
print(glasses)


while overflow == False:
    round = round +1
    print(f"\nRound {round}")
  
    #Ali (us)
    left_over = 1/2
    current_glass = -1
    while left_over != 0:
        current_glass = (current_glass +1)%n
        pour = input(f"How much do you want to pour into glass {current_glass}?  (you can say 'rest')   ")
        if pour == "rest":
            pour = left_over
        else:
           pour = float(pour)

        if pour>left_over:
           print("There's less than that left unfortunately! We'll just add whatever is left")
           pour = left_over
        glasses[current_glass] = glasses[current_glass] + pour
        left_over  = left_over-pour
    print(glasses)
  
    #Check if any glass is overflowing
    for glass in glasses:
      if glass>1:
        print("Ali wins! A glass is overflowing")
        overflow =True
        break
    if overflow == True:
      break
  
    # Beth (bot version)
    a,b = choose_fullest(glasses)
    glasses[a] = 0
    glasses[b] = 0
    print(glasses)
  
