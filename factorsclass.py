def factorsclass():
  class factorial:
      def Find(self, n):
          for i in range(1, n+1):
              if n % i == 0:
                  print(i)

  print("Enter a Number: ", end="")
  try:
      num = int(input())
      print(end="")
      ans = factorial()
      ans.Find(num)
  except ValueError:
    print("Invalid Input!")

if __name__ == "__main__":
    factorsclass()