print("Welcome to the guessing game! To play, guess a number between 1 and 25. Guess correctly to win!")
print("Also, don't guess the same number multiple times.")

while True:
  try:
    difficulty = input("What difficulty do you want? easy or hard?: ")
  except ValueError:
    print("please type 'easy' or 'hard'")
  if difficulty == "easy":
    a = 5
    print("Guess corectly " + str(a) + " times to win!")
    break
  elif difficulty == "hard":
    a = 10
    print("Guess corectly " + str(a) + " times to win!")
    break
  else:
    print("please input 'easy' or 'hard'.")
    
def lvl(a):
  score = 0
  while score < a:
    try:
      ask = int(input("What is your guess?: " ))
    except ValueError:
      print("Please enter a number. Try again!")
      continue
    guesslist = [1, 2, 7, 4, 25, 15, 12, 21, 16, 9]
    guesslist = set(guesslist)
    if ask in guesslist:
      print("You guessed correctly! You got a point!")
      print("The number was " + str(ask))
      score = score + 1
      print("Score: " + str(score))
    elif ask > 25:
      print("That number is too high! Try again!")
    elif ask < 1:
      print("That number is too low! Try agian!")
    else:
      print("Incorrect guess. Try again!")


lvl(a)
print("Congrats! You won!")