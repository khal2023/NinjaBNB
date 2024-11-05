from lib.property import Property

class PropertyRepo:
    pass

# We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection
        self.properties = []
        
    def all(self):
        
        rows = self._connection.execute('SELECT * from properties')
        for row in rows:
            property = PropertyRepo(row["property_name"], row["street_address"], row["city"],row["property_description"], row["price_per_night"], row["host_id"])
            self.properties.append(property)
        return self.properties

# Find an user by host_id
    def find(self, host_id):
        
        rows = self._connection.execute(
            'SELECT * from properties WHERE id = %s', [id])
        row = rows[0]
        return PropertyRepo(row["first_name"], row["surname"], row["username"],row["user_password"])

# Create a new user
    def create (self, users):
        
        self._connection.execute(
            'INSERT INTO users (first_name, surname, username, user_password) VALUES (%s, %s, %s, %s)', 
            [users.first_name, users.surname, users.username, users.user_password]
        )
        return user
    
# Delete an user by their id
    def delete(self, id):
        
        self._connection.execute(
            'DELETE FROM users WHERE id = %s', [id])
        return None