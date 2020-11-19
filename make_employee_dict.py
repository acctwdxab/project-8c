# Dan Wu
# 11/18/2020
# Write a function that take the value of each list and use them to create an Employee object dictionary

class Employee:
    """Represents employee who has name, ID, salary and email"""
    def __init__(self, name, ids, salaries, emails):
        """Create an employee with the specified name, ID, salary and email"""
        self._name = name
        self._ids = ids
        self._salaries = salaries
        self._emails = emails

    def __repr__(self) :
        """returns string of the specified name, ids, salaries and email"""
        return str ( self.name) + ", " + str ( self.ids ) + ", " + str ( self.salaries ) + ", " + str (
            self.emails)

    def get_name(self):
        """Returns employee name"""
        return self.name

    def get_ID_number(self):
     """Returns the employee ID"""
     return self.ids

    def get_salary(self):
        """Returns the employee salary"""
        return self.salaries

    def get_email_address(self):
        """Returns the employee email"""
        return self.emails


def make_employee_dict(name, ids,salaries, emails):
    """to make the dictionary of employees with the specified name, ID, salary and email"""
    employee_dict = {}

    for index in range ( len ( name ) ) :

        employee = Employee ( name[index] , ids[index] , salaries[index] , emails[index] )

        employee_dict[ids[index]] = employee

    return employee_dict


