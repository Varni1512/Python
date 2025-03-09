class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


varni = Employee()
# varni.language = "JavaScript" # This is an instance attribute
varni.greet()
varni.getInfo() 
# Employee.getInfo(varni)
 