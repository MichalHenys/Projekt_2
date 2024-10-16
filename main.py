"""
main.py: druhý projekt do Engeto Online Python Akademie
author: Michal Henyš
email: henysmichal87@gmail.com
discord: Michal Henys
"""
import random

# vytvoření unikátního 4 ciferného čísla, které nezačíná číslem 0
def unique_random_num():
  l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  random.shuffle(l)
  if l[0] == 0:
      pos = random.choice(range(1, len(l)))
      l[0], l[pos] = l[pos], l[0]
  return ''.join(map(str, l[0:4]))

# hlavní volaná funkce
def guessing_numbers():
  print("Hi there!")
  print(47 * "-")
  print("I've generated a random 4 digit number for you.")
  print("Let's play a bulls and cows game.")     

  # volání funkce na generování čísla
  gues_num = unique_random_num()
  print(gues_num)
  num = ""
  guesses = 0
  print(47 * "-")
  print("Enter a number:")

  # Hlavní smyčka ke hře
  while num != gues_num:
    print(47 * "-")
    num = input()

    try:
      x = 0
      y = 0
      guesses += 1

      # ověření hádaného čísla od uživatele, upozornění a pokračování v hádání
      if len(num) != 4 or len(set(num)) != 4: # kontrola délky a duplicit
        print("The number must have exactly 4 unique digits!")
        print("Enter a number:")
        continue
      elif not num.isdigit(): # kontrola, zda se jedná o číslo
        print("Please enter a valid 4-digit number!")
        print("Enter a number:")
        continue
      elif num.startswith('0'): # kontrola, zda nezačíná 0
        print("The number cannot start with 0!")
        print("Enter a number:")
        continue

      # Hlavní cyklus pro zjištění počtu býků a krav, v případě uhodnutí se přičte bod k x nebo y
      for n in range(len(gues_num)):
        if gues_num[n] == num[n]:
          x += 1
        elif gues_num[n] in num:
          y += 1    

      # Uživatel uhodl správné číslo u if
      if num == gues_num:
        print(f"Correct, you've guessed the right number in {guesses} guesses!")
        print(47 * "-")
        break
      # skloňování 
      else:    
        bull_word = "bull" if x == 1 else "bulls"
        cow_word = "cow" if y == 1 else "cows"  
        print(f"{x} {bull_word} and {y} {cow_word}")
    except Exception as e: # zachycení vyjímky
        print(f"An error occurred: {e}")
        continue


guessing_numbers()
