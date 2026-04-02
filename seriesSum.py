# Code that calculates the number of terms in the harmonic series divided by 2
# must be summed to exceed 1
# This will give us an upper bound on how many non adjacent glasses Ali will need in order to win

sum = 0
i=0
while sum <=1:
  i = i+1
  sum= sum +1/(2*i)
  print(i, sum)
