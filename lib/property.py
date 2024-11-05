class Property():
    def __init__(self, id, name, street_address, city, property_description, price_per_night, host_id):
        self.id = id
        self.name = name
        self.street_address = street_address
        self.city = city
        self.property_description = property_description
        self.price_per_night = price_per_night
        self.host_id = host_id
        
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'Property({self.id}, {self.name}, {self.street_address}, {self.city}, {self.property_description}, {self.price_per_night}, {self.host_id})'