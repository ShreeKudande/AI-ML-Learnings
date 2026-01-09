#Q.Create an abstract class Employee with an abstract mothod calculate_salary()
#Create subclasses Intern, FullTimeEmployee, and ContractEmployee that implement the mothod  differently.

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def __init__(self, stipend):
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend
    
class FullTimeEmployee(Employee):
    def __init__(self, base_salary, bonus):
        self.base_salary = base_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus
    
class ContractEmployee(Employee):
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hourly_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hourly_worked
    
i = Intern(100000)
fe = FullTimeEmployee(1200000, 200000)
ce = ContractEmployee(100, 4)

print(i.calculate_salary())
print(fe.calculate_salary())
print(ce.calculate_salary())

