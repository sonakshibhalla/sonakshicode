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

class newFibonacci(): # ethan commit, fibonacci with OOP
  def __init__(self):
    print("1", end=" ") # 0 will always start the sequence
  def __call__(self, n):
    x = 0
    y = 1
    z = 0
    fs = []
    for i in range(n-1):
        z = x + y
        x = y
        y = z
        i += 1
        fs.append(z)



if __name__ == "__main__":
    fibonacci()

  