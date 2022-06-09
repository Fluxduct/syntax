import sys as flx
import sys
import time
import math as maths
import math
from termcolor import colored as coloured
from termcolor import colored

# Log

# def log(entry):
#   if proj == True:
#     logbook = proj

# Console 
def console(concom, coninput1):
  if concom == "write":
    print(coninput1)
  elif concom == "return":
    return coninput1
  
# System
def flx(syscom):
  if syscom == "quit":
    sys.exit()
  
# Time
def time(timecom, timeinput1):
  if timecom == "wait":
    time.sleep(timeinput1)
#  elif timecom == "epoch":
#    console("return", time.time())
  
def pause(pause):
  time.sleep(pause)
def epoch():
  return time.time()

# Artificial Intelligence BANK
# def bank(aicom, aibook, aiinput1):
#   if aicom == "enable":
#     bank=True
#   if aicom == "add":
  
# Mathematics
# def mathematics(mathscom, val1, op, val2):
def triangle(triangle):
  return triangle*(triangle+1)/2
def square(square):
  return square*square
def cube(cube):
  return cube*cube*cube
def sqrt(sq):
  return maths.sqrt(sq)
    
