def factorial(n):   
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
    
def answer():
  num = int(input("Enter a number for factorial: "))
  if num < 0:
      print("factorial does not exist for negative numbers")
  else:
      print(factorial(num))

if __name__ == "__main__":
    answer()