###Homework (29th Sep): purchasing your dream home

## Part I : Calulating time to save 

# Input the user's annual salary
annual_salary = float(input("Enter your annual salary :"))
monthly_salary = annual_salary/12  # Calculate their monthly salary
# Input the user's portion of salary to be saved (the saving rate)
portion_saved = float(input("Enter the portion of salary to be saved :"))
# Input the total cost of the house
total_cost = float(input("Enter the cost of your dream home in Lyon :"))

portion_down_payment = 0.25 # Portion needed for down payment
current_saving = 0 
r = 0.04 # Annual return of investment 
months = 0

while current_saving < total_cost*portion_down_payment:
    if months % 12 == 0 : # Adds the annual return of investment to the savings
        current_saving = current_saving*(1+r)
    saving = monthly_salary*portion_saved
    current_saving += saving 
    months += 1
# Outputs the number of months it will take the user to buy their dream home
print("Number of months: ", months)

"""
Case 1 : 
 With a starting annual salary in Lyon at 60000€, with 10% of your salary saved, if you want to buy a house which costs 400000€, 
 it will take you 157 months.
Case 2 : 
 With a starting annual salary in Lyon at 75000€, with 15% of your salary saved, if you want to buy a house which costs 600000€, 
 it will take you 131 months.
"""
## Part II : Salary raise 

# Input the user's annual salary
annual_salary = float(input("Enter your annual salary :"))
monthly_salary = annual_salary/12  # Calculate their monthly salary
# Input the user's portion of salary to be saved (the saving rate)
portion_saved = float(input("Enter the portion of salary to be saved :"))
# Input the total cost of the house
total_cost = float(input("Enter the cost of your dream home in Lyon :"))
# Input the user's semi-annual salary raise 
semi_annual_raise = float(input("Enter your semi-annual salary raise :"))

portion_down_payment = 0.25 # Portion needed for down payment
current_saving = 0 
r = 0.04 # Annual return of investment 
months = 0

while current_saving < total_cost*portion_down_payment:
    if months % 6 == 0 : # Increases salary every 6 months
        annual_salary *= (1+semi_annual_raise)
    if months % 12 == 0 : # Adds the annual return of investment to the savings
        current_saving = current_saving*(1+r)
    saving = monthly_salary*portion_saved
    current_saving += saving 
    months += 1
print("Number of months: ", months)

"""
 Case 1 : 
 With a starting annual salary in Lyon at 65000€, with 12% of your salary saved and a semi-annual raise of 4%, if you want to buy a house
 which costs 500000€, it will take you 149 months.
 Case 2 :
 With a starting annual salary in Lyon at 80000€ with 10% of your salary saved and a semi-annual raise of 5% 0.10, if you want to buy a house
 which costs 750000€, it will take you 201 months.
"""

## Part III : Finding the right savings rate 

# Input the user's annual salary
annual_salary = float(input("Enter your annual salary: "))

# Constants
total_cost = 1000000  # Total cost of the house
semi_annual_raise = 0.07 # Semi-annual salary raise
portion_down_payment = 0.25  # Portion needed for down payment
r = 0.04  # Annual return on investments
months = 36  # Number of months to save
step = 0

# Function to calculate savings after 36 months given a savings rate
def savings_after_months(portion_saved):
    savings = 0
    monthly_salary = annual_salary / 12  # Calculate the user's monthly salary 
    for month in range(1, months + 1):
        if month % 12 == 0 :  # Adds investment return
            savings += savings * r 
        savings += monthly_salary * portion_saved # Adds current month's savings
        if month % 6 == 0: # Increases salary every 6 months
            monthly_salary += monthly_salary * semi_annual_raise
    return savings

# First we need to check if 100% of the salary is enough, hence the rate will be 1 so 100%
if savings_after_months(1) < total_cost * portion_down_payment:
    print("It is not possible to pay the down payment in three years.")
else:
    # We use bisection search to find the best savings rate
    low, high = 0, 1
    for p in range(100):  # Just a high limit to make sure it's enough
        step +=1
        mid = (low + high) / 2
        current_saving = savings_after_months(mid)
        # Then we check if current savings is close enough to target (more or less 100)
        if abs(current_saving - total_cost * portion_down_payment) <= 100:
            break
        #We adjust search range based on comparison 
        #(between the new low and high value which contains the value we're looking for)
        if current_saving < total_cost * portion_down_payment:
            low = mid
        else:
            high = mid
    # Outputs the best savings rate found and the steps in bisection search
    print(f"Best savings rate: {mid:.4f}")
    print("Steps in bisection search :", step)

"""
Case 1 :
With a starting salry in Lyon at 50000, it is not possible to pay the down payment in three years.
Case 2 :
With a starting salry in Lyon at 90000, the best savings rate is 0.7227 and the number of steps in the bisection search is 8.
Case 3 :
With a starting salry in Lyon at 35000, it is not possible to pay the down payment in three years.
"""

