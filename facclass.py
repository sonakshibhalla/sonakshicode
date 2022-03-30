def facclass():
  num = int(input("Enter a number: "))
  if num < 0:
    print("the input has to be positive")
    return
  class factorial:

    def __call__(self, num):
      if num == "1" or num == "0":
        result = 1
      else: 
        result = 1
        for i in range (num, 1, -1):
          result = result * i
      
      print(result)
      
  answer = factorial()
  answer(num)

if __name__ == "__main__":
    facclass()
