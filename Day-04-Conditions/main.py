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

#Nested If - Else Statement
age = 18
title = "None"
allowed_to_drive = False
driving_license = input("Do you have license ? (Y/N) ").upper() #y
if age >= 18:
    title = "Adult"
    if driving_license == 'Y' :
        allowed_to_drive = True
    else:
        allowed_to_drive = False
else:
    title = "Minor"

print(f"You're {allowed_to_drive} to drive") #You're True to drive

#------------------------------------------------------------
