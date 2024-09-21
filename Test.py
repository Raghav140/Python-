# elif statement
day=str(input("Day:"))
if day == "Monday" or day =="Tuesday" or day =="Wednesday" or day=="Thursday" or day == "Friday":
 print("weekday")
elif day == "Saturday":
 print("its weakend")
elif day == "Sunday":
  print("Its a holiday")
else:
  print("Invalid data")

#looping
for i in range(1,11,3):
  print(i,end=" ")