# Dan Wu
# 11/18/2020
# Write a function that take the value of each list and use them to create an Employee object dictionary,

class Employee:
    """this is the employee class"""
    def __init__(self,emp_names, emp_ids, emp_sals, emp_emails):
        """this is the init method to take four parameters"""
        self.emp_names = emp_names
        self.emp_ids= emp_ids
        self.emp_sals = emp_sals
        self.emp_emails= emp_emails

    def get_name(self):
        """the get methods to get the values of the name"""
        return self.emp_names

    def get_ID_number(self):
     """the get methods to get the values of the employee ID"""
     return self.emp_ids

    def get_salary(self):
        """the get methods to get the values of employee salary"""
        return self.emp_sals

    def get_email_address(self):
        """the get method to get employee email"""
        return self.emp_emails


def make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails):
    """to make the list into employee object"""
    result = {}
    for i in range(len(emp_names)):
        emp = Employee(emp_names[i], emp_ids[i], emp_sals[i], emp_emails[i])
        result[emp_ids[i]] = emp
    return result


