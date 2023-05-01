# In employees.py

from hr import get_policy                       # from hr import PayrollSystem
from productivity import get_role               # from productivity import ProductivitySystem
from contacts import get_employee_address       # from contacts import AddressBook

class _EmployeeDatabase:      # the leading underscore, "_", in "_EmployeeDatabase" class makes it an internal class.  ###You are communicating that the _EmployeeDatabase should not be used directly.  ###This is saying is that the _EmployeeDatabase is a Singleton, and there should only be one object created from it.
    # def __init__(self):
    #     self._employees = [
    #         {
    #             'id': 1,
    #             'name': 'Mary Poppins',
    #             'role': 'manager'
    #         },
    #         {
    #             'id': 2,
    #             'name': 'John Smith',
    #             'role': 'secretary'
    #         },
    #         {
    #             'id': 3,
    #             'name': 'Kevin Bacon',
    #             'role': 'sales'
    #         },
    #         {
    #             'id': 4,
    #             'name': 'Jane Doe',
    #             'role': 'factory'
    #         },
    #         {
    #             'id': 5,
    #             'name': 'Robin Williams',
    #             'role': 'secretary'
    #         },
    #     ]
    #     self.payroll = PayrollSystem()                      #creates an object for the given 'self'
    #     self.productivity = ProductivitySystem()            #creates an object for the given 'self'
    #     self.employee_addresses = AddressBook()             #creates an object for the given 'self'
    def __init__(self):
                self._employees = {
                    1: {
                        'name': 'Mary Poppins',
                        'role': 'manager'
                    },
                    2: {
                        'name': 'John Smith',
                        'role': 'secretary'
                    },
                    3: {
                        'name': 'Kevin Bacon',
                        'role': 'sales'
                    },
                    4: {
                        'name': 'Jane Doe',
                        'role': 'factory'
                    },
                    5: {
                        'name': 'Robin Williams',
                        'role': 'secretary'
                    }
                }
                # No need to instantiate individual (self) self.xyz objects for PayrollSystem(), ProductivitySystem(), and AddressBook()

    @property
    def employees(self):
        # return [self._create_employee(**data) for data in self._employees]      # creates an object (with integer, string, and objects inside of it) for each employee using the unpacked data within their individual dictionary + returns the object as a list.
        return [Employee(id_) for id_ in sorted(self._employees)]               #LIST OF OBJECTS:    sorted(<dictionary>) = a list  ==>  id_ = a value within the list of id's.  The employee id is fed into "Employee()" to return an Employee object for each employee id in the loop.

    # def _create_employee(self, id, name, role):
    #     payroll_policy = self.payroll.get_policy(id)                            #  =  hr.PayrollSystem().get_policy(id)                     ==  SalaryPolicy(3000)  ==  instantiated policy object with data values inside
    #     employee_role = self.productivity.get_role(role)                        #  =  productivity.ProductivitySystem().get_role(role)      ==  ManagerRole()       ==  instantiated IRole (ManagerRole, Secretary Role, etc.)  with NO DATA VALUES inside
    #     address = self.employee_addresses.get_employee_address(id)              #  =  contacts.AddressBook().get_employee_address(id)       ==  Address('121 Admin Rd.', 'Concord', 'NH', '03301')  ==  instantiated Address object with data values inside
    #     return Employee(id, name, address, employee_role, payroll_policy)       #  =  employees.Employee                                    ==  Employee(id,   name,   Address('121 Admin Rd.', 'Concord', 'NH', '03301'),   ManagerRole(),   SalaryPolicy(3000))

    def get_employee_info(self, employee_id):
        info = self._employees.get(employee_id)                                 #self._employees[id]  =  value (which is a dictionary) based on the key = id (id = employee id #)
        if not info:
            raise ValueError(employee_id)
        return info


# In employees.py
from representations import AsDictionaryMixin

class Employee(AsDictionaryMixin):
    # def __init__(self, id, name, address, role, payroll):
    #     self.id = id                # id integer
    #     self.name = name            # name string
    #     self.address = address      # Address() object                                                                      ---  Address('121 Admin Rd.', 'Concord', 'NH', '03301')
    #     self._role = role            # ManagerRole() Interface object        <---- or similar role   policy  ("IRole")       ---
    #     self._payroll = payroll      # SalaryPolicy() Interface object       <---- or similar salary policy  ("IPayroll")    --- SalaryPolicy(3000)
    def __init__(self, id):
        self.id = id                                                            #INTEGER:       name is an integer within the dictionary, self._employees
        info = employee_database.get_employee_info(self.id)                     #DICTIONARY:    self._employees[id]  =  value (which is a dictionary) based on the key = id (id = employee id #)
        self.name = info.get('name')                                            #VALUE:         <dictionary>['name'] = value   ; <dicionary> = DICTIONARY
        self.address = get_employee_address(self.id)                            #OBJECT:        instantiated Address object with data values inside (you now have access to the employee id's street, street2, city, state, zipcode + a __str__)
        self._role = get_role(info.get('role'))                                 #OBJECT:        instantiated IRole (ManagerRole, Secretary Role, etc.)  with NO DATA VALUES inside (you now have access to the employee role's perform_duties() )  ; <dicionary> = DICTIONARY
        self._payroll = get_policy(self.id)                                     #OBJECT:        instantiated policy object with data values inside based on the specific Role Policy

    def work(self, hours):
        duties = self._role.perform_duties(hours)                               #STRING:        string print out    ---- ManagerRole.perform_duties(hours)  <--- [you can access the "ManagerRole" direcly since "self._role = get_role(info.get('role'))"  created the link] by doing ---> instantiated IRole (ManagerRole, Secretary Role, etc.)  with NO DATA VALUES inside (you now have access to the employee role's perform_duties() )
        print(f'Employee {self.id} - {self.name}:')                             #               prints a string
        print(f'- {duties}')                                                    #               prints STRING ("duties")
        print('')
        # print("B=~=~=~=~=~=~=~", self._payroll.hours_worked)
        self._payroll.track_work(hours)                                         #NONE:          nothing returned, just a computation done for record keeping.  ---- SalaryPolicy.track_work(hours), which "track_work" method is inherited from PayrollPolicy  <--- [you can access the "SalaryPolicy" direcly since "self._payroll = get_policy(self.id)"  created the link] by doing ---> instantiated policy object with data values inside based on the specific Role Policy
        # print("A=~=~=~=~=~=~=~", self._payroll.hours_worked)

    def earnings(self):
        return self._payroll.calculate_payroll()     # SalaryPolicy(3000).calculate_payroll()    via Interface object        <---- or via similar salary policy  ("IPayroll")  #     ---- SalaryPolicy.calculate_payroll()  <--- [you can access the "SalaryPolicy" direcly since "self._payroll = get_policy(self.id)"  created the link] by doing ---> instantiated policy object with data values inside based on the specific Role Policy

    def apply_payroll_policy(self, new_policy):         #For an individual Employee object: applies the existing payroll policy to the new policy and then substitutes it.
        new_policy.apply_to_policy(self._payroll)       #LINK:                                    Creates/Initializes a new Employee object, self._base_policy, which is a link/connection to the original Payroll Policy object for the given employee, which is to be used to override the actions (calculate wage, etc).  This can be accessed later when executing actions on the employee data.
        self._payroll = new_policy                      #OBJECT (original) within a new OBJECT:   1) This overrides the original __init__ attribute.  2) A Payroll Policy object, LTDPolicy, <--- with a link inside of it that has the ---> original Payroll Policy, self._base_policy object.  *This is essentially a way to take the original object and extend it below a new object.
        # print(self._payroll._base_policy)

employee_database = _EmployeeDatabase()                                         #OBJECT:        instantiated employee database object with all employee data inside in the form of an integer, dictionary, value, and 3 objects. Also, there are several exposed methods that can be accessed.
