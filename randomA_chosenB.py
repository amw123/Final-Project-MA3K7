import numpy as np
import random

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

  #Ali (bot) - random distribution
  left_over = 1/2
  for i in range(n-1):
    pour = random.random()*left_over
    glasses[i] = glasses[i] + pour   #is this a fair system to randomly distribute the 1/2 pint?
    left_over  = left_over-pour
  glasses[n-1] = glasses[n-1] + left_over 
  print(glasses)

  #Check if any glass is overflowing
  for glass in glasses:
    if glass>1:
      print("Ali wins! A glass is overflowing")
      overflow =True
      break
  if overflow == True:
    break

  #Beth (us)
  choice = input("Which glasses should we empty? eg '1,2'")
  empty_1 = int(choice[0])
  #if error then try again
  empty_2 = int(choice[2])
  #if error then try again
  if (abs(empty_1 -empty_2) != 1) and (abs(empty_1 -empty_2) != n-1):
    print("choose again")
  glasses[empty_1] = 0
  glasses[empty_2] = 0
  print(glasses)
