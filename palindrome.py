def palindrome():
  class Palindrome(object): 
      def function(self, a_string): 
          self.a_string = a_string 
          len_a = len(self.a_string) 
          x = int(len_a / 2) 
 
          if self.a_string[0:x] == self.a_string[-1:-x - 1:-1]: 
              print("This is a Palindrome String") 
          else: 
              print("This is not a Palindrome String") 
 
 
  x = input("Enter the String: ")  
  Object = Palindrome() 
  
  Object.function(x)

if __name__ == "__main__":
    palindrome()

