from lib.users import Users

class UsersRepo:
    def __init__(self, connection):
        self._connection = connection

    def find(self, users_id):
        rows = self._connection.execute('SELECT * FROM users WHERE id = %s', [users_id])
        row = rows[0]
        return Users(row["id"], row["first_name"], row["surname"], row["username"], None)
    
    def username_in_db(self, username):
        rows = self._connection.execute('SELECT username FROM users WHERE username = %s', [username])
        return len(rows) > 0

    def password_is_valid(self, password):
        return len(password) > 7 and any(char in "?!#%&$" for char in password)
    
    def create(self, first_name, surname, username, password):
        if not self.username_in_db(username) and self.password_is_valid(password):
            self._connection.execute('INSERT INTO users (first_name, surname, username, user_password) VALUES (%s, %s, %s, %s)', [
                first_name, surname, username, password])
    

