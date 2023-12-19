from abc import ABC, abstractmethod
from typing import List


class Employee(ABC):
    @abstractmethod
    def do_work(self):
        pass


class Designer(Employee):
    def do_work(self):
        print("Designing architecture.")


class Programmer(Employee):
    def do_work(self):
        print("Coding")


class Company:
    def __init__(self):
        self.employees: List[Employee] = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def create_software(self):
        for employee in self.employees:
            employee.do_work()


FRAUDIO = Company()
FRAUDIO.add_employee(Designer())
FRAUDIO.add_employee(Programmer())
FRAUDIO.create_software()
