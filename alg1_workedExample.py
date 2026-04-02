# N=4,   alpha = 0.01 fully explained example

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

    # take the best adjacent value
    best_max = np.where(adjacent_g == max(adjacent_g))[0][0]//2
    best_max = max_positions[best_max]
    side = np.where(adjacent_g == max(adjacent_g))[0][0]%2
    if side == 0: #left
      best_adjacent = (best_max -1)%len(arr)
      return int(best_adjacent), int(best_max)
    else: #right
      best_adjacent = (best_max +1)%len(arr)
      return int(best_max),int(best_adjacent)


n= 8
alpha = 0.01 # can be anything we choose as long as it 
glasses = np.zeros(n)
overflow =  False
round =0

# We play as Ali
# Beth is the robot
print("Glasses initially:")
print(glasses)


while overflow == False:
    round = round +1
    print(f"\n------------------\nRound {round}\n")

    #Ali (established algorithm #1)
    N= 4
    glasses[2*(N-round)+1] = glasses[2*(N-round)+1] + (0.5-alpha)/(N+1-round) + alpha
    for i in range(N-round):
      glasses[2*i+1] = glasses[2*i+1] + (0.5-alpha)/(N+1-round)
      print(f"Ali adds {(0.5-alpha)/(N+1-round)} to glass {2*i+1}")
    print(f"Ali adds {(0.5-alpha)/(N+1-round) + alpha} to glass {2*(N-round)+1}")
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
    print(f"\nBeth empties glasses {a} and {b}")
    glasses[a] = 0
    glasses[b] = 0
    print(glasses)
  
