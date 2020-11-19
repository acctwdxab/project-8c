# Dan Wu
# 11/18/2020
# Write a function that take the value of each list and use them to create an Employee object dictionary

class Employee:
    """Represents employee who has name, ID, salary and email"""
    def __init__(self, emp_names, emp_ids, emp_sals, emp_emails):
        """Create an employee with the specified name, ID, salary and email"""
        self. _name = emp_names
        self. _ID_number = emp_ids
        self. _salary = emp_sals
        self. _email_address = emp_emails

    def __repr__(self) :
        """returns string of the specified name, ids, salaries and email"""
        return str ( self._name) + ", " + str ( self._ID_number ) + ", " + str ( self._salary ) + ", " + str (
            self._email_address)

    def get_name(self):
        """Returns employee name"""
        return self._name

    def get_ID_number(self):
     """Returns the employee ID"""
     return self._ID_number

    def get_salary(self):
        """Returns the employee salary"""
        return self._salary

    def get_email_address(self):
        """Returns the employee email"""
        return self._email_address


def make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails):
    """to make the dictionary of employees with the specified name, ID, salary and email"""
    employee_dict = {}

    for index in range ( len ( emp_names) ) :

        employee = Employee ( emp_names[index] , emp_ids[index] , emp_sals[index] , emp_emails[index] )

        employee_dict[emp_ids[index]] = employee

    return employee_dict

