def create_student_dict(name, age, major):
    student_dict = {}

    student_dict["name"] = name
    student_dict["age"] = age
    student_dict["major"] = major

    return student_dict

#Output:
{'name': 'Alice', 'age': 20, 'major': 'Computer Science'}

#Accessing the values
country_capitals = {
 "USA": "Washington, D.C.",
 "France": "Paris",
 "Japan": "Tokyo"
}

# Accessing values using keys
print(country_capitals["USA"])
print(country_capitals["France"])

#Output:
Washington, D.C.
Paris
