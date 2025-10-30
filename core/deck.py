def build_standard_deck():
  list_deck=[]
  list=['2','3','4','5','6','7','8','9','10','j','q','k','a']
  for i in list:
    for j in ['h','c','d','s']:
      deck={'rank':i,'suite':j}
      list_deck.append(deck)
  return list_deck

import random

def shuffle_by_suit(deck: list[dict], swaps: int = 5000):
  counter=0
  while counter<swaps:
    j=random.randint(0,51)
    k=random.randint(0,51)
    if j!=k:
      if deck[j]['suite']=='h':
        if k % 5==0:
          deck[j],deck[k]=deck[k],deck[j]
          counter+=1
      if deck[j]['suite'] == 'c':
        if k % 3 ==0:
          deck[j], deck[k] = deck[k], deck[j]
          counter += 1
      if deck[j]['suite'] == 'd':
        if k % 2 ==0:
          deck[j], deck[k] = deck[k], deck[j]
          counter += 1
      if deck[j]['suite'] == '':
        if k % 7 ==0:
          deck[j], deck[k] = deck[k], deck[j]
          counter += 1
  return deck

