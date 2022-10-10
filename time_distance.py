one = input("what do you want to find?distance/speed/time=")
if(one=="distance"):
  speed = int((input("Enter the speed in miter/second")))
  time = int(input("Enter the time in seconds:"))
  distance=speed*time 
  print("The distance calculated for given speed and time is",distance)

elif(one=="speed"):
  distance = int((input("Enter the speed in miter/second")))
  time = int(input("Enter the time in seconds:"))
  speed = distance/time
  print("The distance calculated for given speed and time is",speed)

elif(one=="time"):
  speed = int((input("Enter the speed in miter/second")))
  distance = int(input("Enter the time in seconds:"))
  time = distance/speed
  print("The distance calculated for given speed and time is",time)
  
else:
  print("Enter valid")

