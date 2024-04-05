
# ----------- QUESTION 1 ----------- 

print("""___________      .__        
\_   _____/______|__| ____  
 |    __)_\_  __ \  |/ ___\ 
 |        \|  | \/  \  \___ 
/_______  /|__|  |__|\___  >
        \/               \/ """)

# -----------  QUESTION 2 -----------
side1 = float(input("Hello, this is a triangle area generator, please enter the first side length:"))   

side2 = float(input("please enter the second side length:"))
   
side3 = float(input("please enter the third side length:"))

s = ((side1 + side2 + side3)/2)

import math 
a = round(math.sqrt(s*(s-side1)*(s-side2)*(s-side3)),2)

print(a)


# -----------  QUESTION 3 ----------- 
x=int(input("Hello, please enter your total budget:"))

import random

food = random.randint(20,25)
p = (food/100)
tp = 100
tp = tp-food
f = (x*p)
print("food will be", round((p*100)), "% and cost $", (f)) 
xr = x-f
print("You have ", xr, "remaining and ", tp, "% of your budget.")



clothing = random.randint(25,30)
pclothing = (clothing/100)
tpclothing = 100
tpclothing = tpclothing-clothing-food
fclothing = ((x-f)*pclothing)
print("clothing will be", round((pclothing*100)), "% and cost $", (fclothing)) 
xa = xr-fclothing
print("You have ", xa, "remaining and ", tpclothing, "% of your budget.")


rent = random.randint(35,40)
prent = (rent/100)
tprent = 100
tprent = tprent-rent-food-clothing
frent = ((x-f-fclothing)*prent)
print("rent will be", round((prent*100)), "% and cost $", (frent)) 
xb = xa-frent
print("You have ", xb, "remaining and ", tprent, "% of your budget.")



entertainment = (100-rent-clothing-food)
pentertainment = (entertainment/100)
tpentertainment = 100
tpentertainment = tpentertainment-entertainment-clothing-food-rent
fentertainment = ((x-f-fclothing-frent)*pentertainment)
print("entertainment will be", round((pentertainment*100)), "% and cost $", (xb)) 
xc = xb-xb
print("You have ", round(xc), "remaining and ", tpentertainment, "% of your budget.")
