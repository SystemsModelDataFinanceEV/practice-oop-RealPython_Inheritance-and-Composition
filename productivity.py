# In productivity.py

class _ProductivitySystem:      # the leading underscore, "_", in "_ProductivitySystem" class makes it an internal class.  ###You are communicating that the _ProductivitySystem should not be used directly.  ###This is saying is that the _ProductivitySystem is a Singleton, and there should only be one object created from it.
    def __init__(self):
        self._roles = {
            'manager': ManagerRole,
            'secretary': SecretaryRole,
            'sales': SalesRole,
            'factory': FactoryRole,
        }

    def get_role(self, role_id):
        role_type = self._roles.get(role_id)
        if not role_type:
            raise ValueError('role_id')
        return role_type()     #instantiated IRole (ManagerRole, Secretary Role, etc.)  with NO DATA VALUES inside

    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('==============================')
        for employee in employees:                                              #for each OBJECT (employee) within the LIST OF OBJECTS (employees)
            employee.work(hours)                                                #prints out some strings and does an internal record keeping for "track_work"   ----   employee.work() = employees.Employee.work()
        print('')


# In productivity.py

class ManagerRole:
    def perform_duties(self, hours):
        return f'screams and yells for {hours} hours.'

class SecretaryRole:
    def perform_duties(self, hours):
        return f'does paperwork for {hours} hours.'

class SalesRole:
    def perform_duties(self, hours):
        return f'expends {hours} hours on the phone.'

class FactoryRole:
    def perform_duties(self, hours):
        return f'manufactures gadgets for {hours} hours.'

###############################################################################
#INTERFACE:

_productivity_system = _ProductivitySystem()                                    #internal variable to the module.

def get_role(role_id):                                                          #a public interface to the module
        return _productivity_system.get_role(role_id)                           #instantiated IRole (ManagerRole, Secretary Role, etc.)  with NO DATA VALUES inside (you now have access to the employee role's perform_duties() )

def track(employees, hours):                                                    #a public interface to the module
    _productivity_system.track(employees, hours)                                #prints out some strings and does an internal record keeping for "track_work"   ----   employee.work() = employees.Employee.work()
###############################################################################
