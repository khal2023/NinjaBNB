class User:
    def __init__(self, user_id, first_name, surname, username, password):
        self.user_id = user_id
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
