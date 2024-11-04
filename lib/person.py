class Person:
    def __init__(self, person_id, first_name, surname, username, password):
        self.person_id = person_id
        if isinstance(first_name, str):
            self.first_name = first_name
        else:
            raise Exception("String inputs only")
        if isinstance(surname, str):
            self.surname = surname
        else:
            raise Exception("String inputs only")
        if isinstance(username, str):
            self.username = username
        else:
            raise Exception("String inputs only")
        if isinstance(password, str):
            self.password = password
        else:
            raise Exception("String inputs only")
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Person({self.person_id}, {self.username})"
