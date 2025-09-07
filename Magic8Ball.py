#Magic8Ball.py
#Name: Grant Schaeffer
#Date: 9/7/25
#Assignment: Lab 2.1

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")

  #Prompt the user for their question.

  input("Ask a question about your day: ")

  options = ["As I see it yes", "Ask again later", "It is decidedly so", "Yes, definitely",
              "Perchance", "Only a fool would believe that", "Unless you are a Husker fan, no",
              "I would not hold onto hope", "Only if mamma says it's okay"]

  #Answer question randomly with one of the options from your earlier list.
  length = len(options)

  a = random.random() * length

  a = int(a)

  response = options[a]

  print(response)

if __name__ == '__main__':
  main()
