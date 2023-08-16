class Employee:

    def __init__(self, name,salary,designation):
        self.name = name
        self.salary = salary
        self.designation = designation

    def __str__(self):
        return f"name : {self.name}, salary : {self.salary}, designation : {self.designation}"

    def max_salary_employee(emplist):
        max = -1
        max_em
       
        for employee in emplist:
            if employee.salary > max:
                max = employee.salary
                max_em = employee

        return max_em




