#-----------------------------------------------------------------------------------------------#
'''
WRAPPERS:  wrappers used for the program
'''

def wrapprint(a):
    print("####################################################################################")
    return a()

#################################################################################################
#-----------------------------------------------------------------------------------------------#
# # In program.py
#
# @wrapprint
# def function_v21():
#     from hr import PayrollSystem, HourlyPolicy
#     from productivity import ProductivitySystem
#     from employees import EmployeeDatabase
#
#     productivity_system = ProductivitySystem()
#     payroll_system = PayrollSystem()
#     employee_database = EmployeeDatabase()
#
#     employees = employee_database.employees                 #   =  employees.EmployeeDatabase().employees                   ==  creates an object (with integer, string, and objects inside of it) for each employee using the unpacked data within their individual dictionary + returns the object as a list.
#     #You can change the Employee data if you want  ---->   employees[0].payroll = HourlyPolicy(55)
#     productivity_system.track(employees, 40)                #   =  productivity.ProductivitySystem().track(employees, 40)   ==  prints some things       #   =  ProductivitySystem().track(EmployeeDatabase().employees, 40)
#     payroll_system.calculate_payroll(employees)             #   =  hr.PayrollSystem().calculate_payroll(employees)              #   =  PayrollSystem().calculate_payroll(EmployeeDatabase().employees)
#
#     return None
#
# #-----------------------------------------------------------------------------------------------#
# # In program.py
#
# @wrapprint
# def function_v22():
#     import json
#     from employees import EmployeeDatabase
#
#     def print_dict(d):
#         print(json.dumps(d, indent=2))
#
#     for employee in EmployeeDatabase().employees:
#         print_dict(employee.to_dict())
#
#     return None
# #-----------------------------------------------------------------------------------------------#
# '''
#    Calling Functions to execute the program
# '''
#
# function_v21
# function_v22

#-----------------------------------------------------------------------------------------------#
'''
V3: V2 + Composition

a single Employee object can be created from its id

You are using composition in two different ways.
   1) The Address class provides additional data to Employee
   2) The role and payroll objects provide additional behavior within Employee.
   Still, the relationship between Employee and those objects is loosely coupled, which provides some interesting capabilities that you’ll see in the next section.
'''
'''
  NOTES:
    You are basically saying that there should only be one _AddressBook, one _PayrollSystem, and one _ProductivitySystem. Again, this design pattern is called the Singleton design pattern
'''

    #---------------------------------------------------------------------#
    #Execute this code:
    #   1) create the employees based on the data fed into the EmployeeDatabase, the empolyee ID#
    #   2) then, you can perform actions based on the employees' information
@wrapprint
def function_v30():
    from employees import employee_database
    from productivity import track
    from hr import calculate_payroll, LTDPolicy
    # print("AFTER $$$$$$$$$$$$$$$$$$$$$$$$")
    #---------------------------------------------------------------------#
    #EMPLOYEE SETTINGS & DATA
    ## *** The EmployeeDatabase  (all Employee objects stored within a list, "employees property/attribute") is what EVERYTHING must go through to deal with anythin related to an/the employee(s)
    employees = employee_database.employees                                     #OBJECT:    instantiated employee database object with all employee data inside in the form of an integer, dictionary, value, and 3 objects. Also, there are several exposed methods that can be accessed.

    #changing  self._payroll  to a new value (value within the self._payroll object, that is)
    #Creates/Initializes a new Employee object, self._base_policy.  This can be accessed later when executing actions on the employee data.
    sales_employee = employees[2]                                               #OBJECT:    employee OBJECT
    ltd_policy = LTDPolicy()
    print(ltd_policy)
    sales_employee.apply_payroll_policy(ltd_policy)                             #OBJECT:    instantiated policy object with data values inside based on the specific Role Policy

    #---------------------------------------------------------------------#
    #EXECUTING ACTIONS BASED ON THE EMPLOYEE SETTINGS & DATA
    track(employees, 40)                                                        #prints out some strings and does an internal record keeping for "track_work"   ----   employee.work() = employees.Employee.work()
    calculate_payroll(employees)                                                #retrieves the payroll (goes from "_PayrollSystem.calculate_payroll()", which connects to "employees.earnings()" , which then connects to "SalaryPolicy.calculate_payroll()")

    #---------------------------------------------------------------------#
    # EXTRA:  you can print data of an employe via their employee id #
    from employees import employee_database, Employee
    import json

    def print_dict(d):
        print(json.dumps(d, indent=2))

    temp_secretary = Employee(5)
    print('Temporary Secretary:')
    print_dict(temp_secretary.to_dict())

#-----------------------------------------------------------------------------------------------#
'''
   Calling Functions to execute the program
'''

function_v30

#-----------------------------------------------------------------------------------------------#
