#FutureTime.py
#Name: Grant Schaeffer
#Date: 9/7/25
#Assignment: Lab 2.2

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = now.hour
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  New_Hours = input("Hwo many hours will be added? ")

  #Ask user for minutes
  New_Minutes = input("How many minutes will be added? ")

  a = int(New_Hours)
  b = int(New_Minutes)

  #Calculate the time after the user-supplied time has passed.
  Future_Minutes = (currentMinute + b) % 60
  
  Extra_Hour = (currentMinute + b) // 60

  Final_Hour = (currentHour + a + Extra_Hour) % 24

  print(Final_Hour , ":" , Future_Minutes)

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()
