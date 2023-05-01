# In representations.py

class AsDictionaryMixin:
    def to_dict(self):
        # print("\n~=~=~=~=~= ", self.__dict__.items(),'\n')
        # [print(prop, self._represent(value),"~=~=~=~=~= ") for prop, value in self.__dict__.items() if not self._is_internal(prop)]
        return {
            prop: self._represent(value)
            for prop, value in self.__dict__.items()
            if not self._is_internal(prop)
        }

    def _represent(self, value):                                                    #this function checks if the value is a string (which came from a dictionary) or an object (ex = there is an Address object with EmployeeDatabase().employees  ----- this Address Class that made this Address object and the Employee Class both inherit the mixin class for creating dictionaries).
        if isinstance(value, object):
            if hasattr(value, 'to_dict'):                                           #the object will trigger this since the Address object inherited the mixin program and therefore has a .to_dict() attribute that was instantiated within the object.
                # print('-Y----------------------------------------------------')
                return value.to_dict()                                              #the Address object from within the Employee object will get set to the function, to_dict, as if it were nested within Employee, which it is.
            else:
                # print('-N----------------------------------------------------')
                return str(value)
        else:
            return value

    def _is_internal(self, prop):
        return prop.startswith('_')
