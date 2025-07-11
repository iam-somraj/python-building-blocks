#If Statement
age = int(input("Enter your age: ")) #20
status = "Child"
if age > 18:
    status = "Adult"

print(f"You're a {status}") # You're a Adult

#----------------------------------------------------------

#If - Else Statement
wind = int(input()) #20
status = "undefined"

if wind < 8:
    status = "Calm"
elif wind >= 8 and wind <= 63:
    status = "Breeze"
else:
    status = "Storm"          

print(f"status = {status}") #Breeze

#-----------------------------------------------------------
