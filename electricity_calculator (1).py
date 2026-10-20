# Electricity Bill Calculator
RATE = 12.90
while True:
    name = input("Enter customer name(must not be empty): ")

    if name.strip() != "":
        break

    else: 
        print("name required, must not be empty.")

while True:    
    previous = input("Enter previous meter reading(must atlest be 0): ")
    
    if previous.isdigit() and 0 <= int(previous) <=100:
        previous = int(previous)
        break
    elif previous == "":
        print("Please input a number from 0 to 100")
    else:
        print("Please input a valid number")

while True:
    current = input("Enter current meter reading(same amount or higher than the previous reading): ")
    
    if current.isdigit() and 0 <= int(current) <=100:
        current = int(current)
        break
    elif current > previous:
        print("Enter a number greater than or equal to previous reading.")
    else:
        print("enter a valid number.")


consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))

















