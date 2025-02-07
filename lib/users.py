class Users:
    def __init__(self, users_id, first_name, surname, username, password=None):
        self.users_id = users_id
        self.first_name = self._validate_string(first_name)
        self.surname = self._validate_string(surname)
        self.username = self._validate_string(username)
        if password is not None:
            self.password = self._validate_string(password)
        else:
            self.password = None
    
    def _validate_string(self, value):
        if not isinstance(value, str):
            raise Exception(f"String inputs only")
        return value
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Users({self.users_id}, {self.username})"
