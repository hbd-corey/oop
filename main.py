class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"


    def fullname(self):
        return f"{self.first} {self.last}"


emp_1 = Employee("Johnny", "Bydlak", 50000)
emp_2 = Employee("Test", "User", 60000)



#
