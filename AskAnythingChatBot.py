import wikipedia
import wolframalpha

while True:
  input =  raw_input("Q:")
  
  #Wolfralpha
  try:
    app_id = "V82UAG-4WUVP55EQE"#deactivated
    client = wolframalpha.Client(app_id)
    res = client.query(input)
    answer = next(res.results).text
    print answer

  #Wikipedia
  except:  
    print wikipedia.summary(input)