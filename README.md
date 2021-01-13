# roulette_python

simlified roulette game in Python

**Simlified rules:**

* 0-36: random number of the ball
* 0: loses
* Odd number: Red/Rouge
* Even number: Black/Noir


**Code logic:**

1. Ask

1. bet_at = your bet on:"Faites vos jeux [1-36]”, ‘R’ouge ,’N’oir, e’x’it

   1. Check input, ask again if wrong
   2. bet_amount = Your bet $:
      1. Check input, ask again if wrong
      2. wallet_amount -= bet_amount
2. "Faites vos jeux"
   import random
   ball_at = random.uniform(0, 36)
3. If ball_at ==0

   1. print uraf looser
4. elif bet_at == ‘r’ # rouge -> red

   1. if ball_at & 1 == 1 # is odd?
      1. win_amount = bet_amount * 2
5. elif bet_at == ‘n’ # noir -> even

   1. if ball_at & 1 == 0 # is even
      1. win_amount = bet_amount * 2
6. elif int(bet_at) == ball_at

   1. win_amount = bet_amount * 36
7. If win_amount > 0

   1. wallet_amount += win_amount
8. Print wallet_amount

   1. else Print you lost & wallet_amount
