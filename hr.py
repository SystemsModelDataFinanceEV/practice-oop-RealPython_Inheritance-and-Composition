# In hr.py

class _PayrollSystem:      # the leading underscore, "_", in "_PayrollSystem" class makes it an internal class.  ###You are communicating that the _PayrollSystem should not be used directly.  ###This is saying is that the _PayrollSystem is a Singleton, and there should only be one object created from it.
    def __init__(self):
        self._employee_policies = {
            1: SalaryPolicy(3_000),
            2: SalaryPolicy(1_500),
            3: CommissionPolicy(1_000, 100),
            4: HourlyPolicy(15),
            5: HourlyPolicy(9)
        }

    def get_policy(self, employee_id):
        policy = self._employee_policies.get(employee_id)
        if not policy:
            return ValueError(employee_id)
        return policy   #instantiated policy object with data values inside

    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'Role: {employee._role}')  #<--- cannot return the role because of the way that the database is setup (no read-write)')
            print(f'- Check amount: {employee.earnings()}')            #this connects to "employees.calculate_payroll()" , which then connects to "SalaryPolicy.calculate_payroll()"
            if employee.address:
                print('- Sent to:')
                print(employee.address)
            print('')

# In hr.py

class PayrollPolicy:
    def __init__(self):
        self.hours_worked = 0

    def track_work(self, hours):
        self.hours_worked += hours

class SalaryPolicy(PayrollPolicy):
    def __init__(self, weekly_salary):
        super().__init__()
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class HourlyPolicy(PayrollPolicy):
    def __init__(self, hour_rate):
        super().__init__()
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate

class CommissionPolicy(SalaryPolicy):
    def __init__(self, weekly_salary, commission_per_sale):
        super().__init__(weekly_salary)
        self.commission_per_sale = commission_per_sale

    @property
    def commission(self):
        sales = self.hours_worked / 5
        return sales * self.commission_per_sale

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission


# In hr.py

class LTDPolicy:
    def __init__(self):
        self._base_policy = None

    def apply_to_policy(self, base_policy):                                     #Creates/Initializes a new Employee object, self._base_policy, which is a link/connection to the original Payroll Policy object for the given employee, which is to be used to override the actions (calculate wage, etc).  This can be accessed later when executing actions on the employee data.
        self._base_policy = base_policy

    def track_work(self, hours):                                                #Does NO modifications
        self._check_base_policy()
        return self._base_policy.track_work(hours)

    def calculate_payroll(self):                                                #Modifies the base_salary value used to compute earnings
        self._check_base_policy()
        base_salary = self._base_policy.calculate_payroll()
        return base_salary * 0.6

    def _check_base_policy(self):       #an internal ._check_base_policy() method that raises an exception if the ._base_policy has not been applied.
        if not self._base_policy:
            raise RuntimeError('Base policy missing')


###############################################################################
#INTERFACE:

_payroll_system = _PayrollSystem()                                              #internal variable to the module.

def get_policy(employee_id):                                                    #a public interface to the module
    return _payroll_system.get_policy(employee_id)                              #instantiated policy object with data values inside based on the specific Role Policy

def calculate_payroll(employees):                                               #a public interface to the module
    _payroll_system.calculate_payroll(employees)                                #retrieves the payroll (goes from "_PayrollSystem.calculate_payroll()", which connects to "employees.earnings()" , which then connects to "SalaryPolicy.calculate_payroll()")
###############################################################################
