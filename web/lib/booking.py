class Booking:
    def __init__(self, id, property_id, user_id, start_date, end_date, status):
        self.id = id
        self.property_id = property_id
        self.user_id = user_id
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
    
    def __eq__(self, other):
        if not isinstance(other, Booking):
            return False
        
        return (
            self.id == other.id and
            self.property_id == other.property_id and
            self.user_id == other.user_id and
            str(self.start_date) == str(other.start_date) and
            str(self.end_date) == str(other.end_date) and
            self.status == other.status
        )

    def __repr__(self):
        return f"Booking({self.id}, {self.property_id}, {self.user_id}, {self.start_date}, {self.end_date}, {self.status})"
