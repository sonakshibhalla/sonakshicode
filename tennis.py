import time
import os

CourtColor = "\u001B[32m"

def tennis1():
    print("    ____      ")
    print("   /    |           ____ ")
    print("   \   /           /    \ ")
    print("  /  /             ------ ")
    print("  __               \____/ ")
    print("\u001b[32m \u001b[32m")

def tennis2(): 
    print("    ____      ")
    print("   /    |     ____ ")
    print("   \   /     /    \ ")
    print("  /  /       ------ ")
    print("  __         \____/ ")
    print("\u001b[32m \u001b[32m")

def tennis3():
    print("    ____      ")
    print("   /    | ____ ")
    print("   \   / /    \ ")
    print("  /  /   ------ ")
    print("  __     \____/ ")
    print("\u001b[32m \u001b[32m")

def tennis():
  os.system("clear")
  time.sleep(.5)
  tennis1()
  time.sleep(.5)
  os.system("clear")
  tennis2()
  time.sleep(.5)
  os.system("clear")
  tennis3()


if __name__ == "__main__":
    tennis()
 





