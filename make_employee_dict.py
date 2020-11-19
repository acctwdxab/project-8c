# Dan Wu
# 11/18/2020
# Write a function that take the value of each list and use them to create an Employee object dictionary

class Employee:
    """Represents employee who has name, ID, salary and email"""
    def __init__(self, emp_names, emp_ids, emp_sals, emp_emails):
        """Create an employee with the specified name, ID, salary and email"""
        self._emp_names = emp_names
        self._emp_ids = emp_ids
        self._emp_sals = emp_sals
        self._emp_emails = emp_emails

    def __repr__(self) :
        """returns string of the specified name, ids, salaries and email"""
        return str ( self._emp_names) + ", " + str ( self._emp_ids ) + ", " + str ( self._emp_sals ) + ", " + str (
            self._emp_emails)

    def get_name(self):
        """Returns employee name"""
        return self._emp_names

    def get_ID_number(self):
     """Returns the employee ID"""
     return self._emp_ids

    def get_salary(self):
        """Returns the employee salary"""
        return self._emp_sals

    def get_email_address(self):
        """Returns the employee email"""
        return self._emp_emails


def make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails):
    """to make the dictionary of employees with the specified name, ID, salary and email"""
    employee_dict = {}

    for index in range ( len ( emp_names) ) :

        employee = Employee ( emp_names[index] , emp_ids[index] , emp_sals[index] , emp_emails[index] )

        employee_dict[emp_ids[index]] = employee

    return employee_dict

