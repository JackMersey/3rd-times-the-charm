import time

person = raw_input("enter your name: ")

print "Hello," + person

Job = raw_input("So what do you do for a living?: ")

print "I see your a " + Job

time.sleep(1)

age = input("How old are you?: ")

if age <= 30:
  print "Fuck me one foot in the grave!"
else:
  print "I see sounds about right"
  
retire = 60 - age
  
time.sleep(1)

print "so that would mean that your %s from retiring" retire


time.sleep(1)

retire = 60 - age
  
time.sleep(1)

print ("so that would mean that your %s years from retiring;" % retire)

time.sleep(0.003)

print Thats a fair way off
