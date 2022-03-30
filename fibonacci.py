def fibonacci():
    num = input("Enter a number for fibonacci:")
    try:
      num = int(num)
      if num < 0:
        print("The input is not positive")
    except:
      print("The input is not an integer")
    else:
        def fib(num):
           if num <= 1:
             return num
           else:
             return(fib(num-1) + fib(num-2))
        for i in range(num):
            print(fib(i))

def newFibonacci(): # ethan commit, fibonacci with OOP
  def __init__(self):
    print("0", end=" ") # 0 will always start the sequence
  def __call__(self, n):
    for i in range(1, n):
      something
      return 

if __name__ == "__main__":
    fibonacci()

  