def factorsimp():
  def factorial(n):
      for i in range(1, n+1):
          if n % i == 0:
              print(i)
      print()

  print("Enter a Number: ", end="")
  try:
      number= int(input())
      print(end="")
      factorial(number)
  except ValueError:
      print("Invalid Input!")

if __name__ == "__main__":
    factorsimp()