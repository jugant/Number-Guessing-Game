import random
print('number gussing game')
number = random.randint( 1, 9)
chances=0
print("guess a number (between 1 and 9):")

while chances < 5:
  guess = int(input("Enter your guess:- "))


  if guess == number:
    print("congratulation YOU WON!!!")
    break
  
  elif guess < number:
    print("Your guess was too low: Guess a number hight than",guess)

  else:
    print("Yor guess was too hight: Guess a number lower then",guess)

  chances += 1

if not chances < 5:
  print("YOU LOSE!!! The number is",number)