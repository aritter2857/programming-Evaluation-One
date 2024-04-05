#______________________Question 1_______________________________
# print ava
print("""       d8888 888     888     d8888 
      d88888 888     888    d88888 
     d88P888 888     888   d88P888 
    d88P 888 Y88b   d88P  d88P 888 
   d88P  888  Y88b d88P  d88P  888 
  d88P   888   Y88o88P  d88P   888 
 d8888888888    Y888P  d8888888888 
d88P     888     Y8P  d88P     888 


                                   """)

#_______________________Question 2_______________________________
import math
#ask for side lengths
side_1 = float(input("What is the length of side 1? "))
side_2 = float(input("What is the length of side 2? "))
side_3 = float(input("What is the length of side 3? "))

#calculate s
s = (side_1 + side_2 + side_3) / 2
#calculate area
a = math.sqrt(s * (s - side_1) * (s - side_2) * (s - side_3))
print("\n The area of the triangle is", round(a, 2))

#_______________________Question 3_______________________________
import random

#ask user for budget amount
budget = float(input("What is your monthly budget? "))

#generate random numbers
percent1 = random.uniform(0.01, 0.30)
percent2 = random.uniform(0.01, 0.30)
percent3 = random.uniform(0.01, 0.30)
percent4 = 1-percent1-percent2-percent3

clothing = budget*percent1
rent = budget*percent2
food =budget*percent3
entertainment = budget*percent4

w_percent1 = round(percent1*100)
w_percent2 = round(percent2*100)
w_percent3 = round(percent3*100)
w_percent4 = round(percent4*100)


print(\n "Clothing: $", round(clothing, 2),"thats", w_percent1, "% of budget")
print("Rent: $", round(rent, 2),"thats", w_percent2, "% of budget")
print("Food: $", round(food, 2),"thats", w_percent3, "% of budget")
print("Entertainment: $", round(entertainment, 2),"thats", w_percent4, "% of budget")

