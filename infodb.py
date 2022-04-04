def information():   
  InfoDb = [] 
  InfoDb.append({  
                 "FirstName": "Sonakshi",  
                 "LastName": "Bhalla",  
                 "DOB": "Nov 12, 2004",  
                 "Residence": "San Diego",  
                 "Email": "bhallasonakshi@gmail.com",  
                 "Fav_colors":["red", "green", "blue"]  
                }) 
  print(InfoDb)
  
  
  def print_data(n):
      print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])
      print("\t", "Favorite Colors: ", end="")
      print(", ".join(InfoDb[n]["Fav_colors"]))
      print()
    
  def for_loop():
    for n in range(len(InfoDb)):
      print_data(n)
  
  def while_loop(n):
      while n < len(InfoDb):
          print_data(n)
          n += 1
      return
  
  def recursive_loop(n):
      if n < len(InfoDb):
          print_data(n)
          recursive_loop(n + 1)
      return 
  
  def print():
      print("For loop")
      for_loop()
      print("While loop")
      while_loop(0)
      print("Recursive loop")
      recursive_loop(0)
  print()

if __name__ == "__main__":
    information()
