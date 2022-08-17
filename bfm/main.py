import os
import string
from files import fil
print("Type help,")
print()
while(True):
    os.system("clear")
    fl = fil.ls()
    try:
      inp = input()
      inp = inp.strip()
    except:
      print("how tell me hoow!!! you have this error how?")
      print("well i cant have a input from you intresting...")
      input()
    if inp == "fil":
       fil.fil()
    elif inp == "dir":
       fil.dir()
    elif inp == "rm":
       fil.rm(fl)
    elif inp == "up":
       fil.up()
    elif inp == "dwn":
       fil.dwn()
    elif inp == "xx":
      os.system("clear")
      break 
    else:
      print("what?")
      input()