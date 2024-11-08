from lib.property import *

class PropertyRepo:

# We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection
        # self.properties = []
        
    def all(self):
        rows = self._connection.execute('SELECT * from properties')
        properties = []
        for row in rows:
            property = Property(row["id"], row["property_name"], row["street_address"], row["city"],row["property_description"], row["price_per_night"], row["host_id"])
            properties.append(property)
        return properties

    def find(self, property_id):
        rows = self._connection.execute(
            'SELECT * from properties WHERE id = %s', [property_id])
        row = rows[0]
        return Property(row["id"], row["property_name"], row["street_address"], row["city"],row["property_description"], row["price_per_night"], row["host_id"])

    def create (self, properties):
        
        self._connection.execute(
            'INSERT INTO properties (property_name, street_address, city, property_description, price_per_night, host_id) VALUES (%s, %s, %s, %s, %s, %s)', 
            [properties.name, properties.street_address, properties.city, properties.property_description, properties.price_per_night, properties.host_id]
        )
        return None
    
# Delete an user by their id
    def delete(self, property_id):
        
        self._connection.execute(
            'DELETE FROM properties WHERE id = %s', [property_id])
        return None