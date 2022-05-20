

#created class Employee as a parent class
class Employee:
    name = ''
    email = ''
    password = ''
    employee_id = 0

#created Manager1 class, it is the highest tier of manager that falls under the Employee class
class Manager1(Employee):
    security_clearance = 3
    department = ''
    floor = ''

#created Front Desk Associate class, floor and department can be assigned as needed.
class FDAssociate(Employee):
    security_clearance = 0
    department = ''
    floor = ''
