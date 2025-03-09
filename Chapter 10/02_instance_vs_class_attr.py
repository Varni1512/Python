class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000


varni = Employee()
varni.language = "JavaScript" # This is an instance attribute
print(varni.language, varni.salary)
 