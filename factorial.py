def factorial():   
    def fac(n):
      if n == 1 or n == 0:
          return 1
      else:
          return n * fac(n-1)
    num = int(input("Enter a number for factorial: "))
    if num < 0:
        print("factorial does not exist for negative numbers")
    else:
        print(fac(num))

if __name__ == "__main__":
    factorial()