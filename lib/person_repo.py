from lib.person import Person

class PersonRepo:
    def __init__(self, connection):
        self._connection = connection

    def find(self, person_id):
        rows = self._connection.execute('SELECT * FROM people WHERE id = %s', [person_id])
        row = rows[0]
        return Person(row["id"], row["first_name"], row["surname"], row["username"], None)
    
    def username_in_db(self, username):
        rows = self._connection.execute('SELECT username FROM people WHERE username = %s', [username])
        return len(rows) > 0

    def password_is_valid(self, password):
        return len(password) > 7 and any(char in "?!#%&$" for char in password)
    
    def create(self, first_name, surname, username, password):
        if not self.username_in_db(username) and self.password_is_valid(password):
            self._connection.execute('INSERT INTO people (first_name, surname, username, user_password) VALUES (%s, %s, %s, %s)', [
                first_name, surname, username, password])
    

