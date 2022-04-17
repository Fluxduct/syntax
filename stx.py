import sys
import time

# Console Speech
def write(write):
  print(write)
  
# System
def quit():
  sys.exit()
def ver():
  write(sys.version)
  
# Time
def pause(pause):
  time.sleep(pause)
