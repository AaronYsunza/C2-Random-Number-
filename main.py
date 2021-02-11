import random

print("Coin Flip")

# 1 = heads, 2 = tails
coin = random.randint(1,2)

if(coin == 1):
  print("It's heads!")
elif(coin == 2):
  print("It's tails!")

print("Dice Roll")

# Exercise: Create a code that mimics a dice roll using random numbers. The code should print out what number is "rolled", letting the user know what the result

dice = random.randint(1,6)

if(dice == 1):
  print("It landed on 1!")
elif(dice == 2):
  print("It landed on 2!")
elif(dice == 3):
  print("It landed on 3!")
elif(dice == 4):
  print("It landed on 4!")
elif(dice == 5):
  print("It landed on 5!")
elif(dice == 6):
  print("It landed on 6!")