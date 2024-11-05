from lib.person import Person

class PersonRepo:
    def __init__(self, connection):
        self._connection = connection

    def find(self, person_id):
        rows = self._connection.execute('SELECT * FROM people WHERE id = %s', [person_id])
        row = rows[0]
        person = Person(row["id"], row["first_name"], row["surname"], row["username"], row["user_password"])
        return str(person)
