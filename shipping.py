#Jeremaquai's Sals Shipping Script
print("Welcome to Sal's Shipping calculator!!")

weight = input("Enter the weight of your package in pounds:")

#ground shipping
if int(weight) < 2:
  cost = (int(weight) * 1.5) + 20
  print("The cost for ground shipping this package is: $" + str(cost))
elif int(weight) > 2 and int(weight) <= 6:
  cost = (int(weight) * 3) + 20
  print("The cost for ground shipping this package is: $" + str(cost))
elif int(weight) > 6 and int(weight) <= 10:
  cost = (int(weight) * 4) + 20
  print("The cost for ground shipping this package is: $" + str(cost))
else:
  cost = (int(weight) * 4.75) + 20
  print("The cost for ground shipping this package is: $" + str(cost))

premium = 125
print("The cost for Premium ground shipping this package is $" + str(premium))

#Drone Shipping
if int(weight) <= 2:
  cost2 = int(weight) * 4.5
  print("The cost for drone shipping this package is $" + str(cost2))
elif int(weight) > 2 and int(weight) <= 6:
  cost2 = int(weight) * 9
  print("The cost for drone shipping this package is $" + str(cost2))
elif int(weight) > 6 and int(weight) <= 10:
  cost2 = int(weight) * 12
  print("The cost for drone shipping this package is $" + str(cost2))
else:
  cost2 = int(weight) * 14.25
  print("The cost for drone shipping this package is $" + str(cost2))

#cheapest shipping option

if premium < cost and premium < cost2:
    print("Ground shipping premium is your cheapest option!")
elif cost < premium and cost < cost2:
    print("Ground shipping is your cheapest option!")
else:
    print("Drone shipping is your cheapest option!")