import sys
import time

# Console Speech
def write(write):
  print(write)
  
# System
def quit():
  sys.exit()
def ver():
  return sys.version
  
# Time
def pause(pause):
  time.sleep(pause)
def epoch():
  return time.time()
    
  
# Mathematics
def triangle(triangle):
  return triangle*(triangle+1)/2
def square(square):
  return square*square
def cube(cube):
  return cube*cube*cube
def sqrt(sq):
  return sq / sq
    
