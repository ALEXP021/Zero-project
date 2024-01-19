"""Guess the number game.
The computer itself makes a guess and guesses the number itself
"""

import numpy as np



def guess_number(nbr, a1=1, b1=101, count=0) -> int:
  
  """"The guess_number function describes the algorithm for finding the guessed number.
  The arguments of the integer type function are - nbr (the hidden number), arguments with default values: a1 (the border of the left range - initially - 1),
  b1(the border of the right range - initially - 101), count(number of the attempt to guess the number - initially 0).
  The function will return the number of attempts to guess the number - an integer type.
  """

  numb = int((a1+b1)/2) # We try to guess the number - we take the middle of the range a1-b1 rounded to a whole number - the numb variable.


  if numb == nbr:   # We check whether the value nbr is equal to the hidden number.
    count+=1        # If yes - equal, then we increase the number of guessing attempts by 1 and return them.    
    return count

  elif numb > nbr:           # If the hidden number is less than the middle number of the range.
    count+=1                 # We increase the number of guessing attempts by 1

    b1 = int((a1+b1)/2)      # We reduce the number guessing range by half; the right boundary of the new range will be the middle of the old range.


  elif numb < nbr:           # If the hidden number is more than the middle number of the range.
    count+=1                 # We increase the number of guessing attempts by 1
    
    a1 = int((a1+b1)/2)      # We reduce the number guessing range by half; the left boundary of the new range will be the middle of the old range.


  return(guess_number(nbr,a1,b1,count))   # We recursively run the guess_number function and pass in the guessed number, 
                                          # the new narrowed range limits for guessing the number, and the number of attempts we have already spent.



def test_alg() -> int:
  
  """"The test_alg function is used to test the algorithm described in the guess_number function in a sample of 1000 attempts.
  The function will return the average number of attempts to guess the given number - an integer type.
  """
  
  count_ls = []    # We will add the results of testing the algorithm of function guess_number to the count_ls list - the number of guessing attempts.

  for i in range(1,10001):                  # We start a cycle of attempts to test the function guess_number algorithm - 1000 attempts.
    number = np.random.randint(1, 101)      # We randomly select a number from 1 to 100
    count_ls.append(guess_number(number))   # We run the guess_number function and write the result of its testing to the count_ls list

  score = int(np.mean(count_ls))            # We calculate the average number of values ​​in the count_ls list/
  return (score)                            # We reduce the average value of attempts to guess a number over a sample of 1000 tests




if __name__ == "__main__":
    # RUN
    test_alg()     # We are launching the function test_alg
