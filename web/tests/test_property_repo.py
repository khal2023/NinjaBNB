from lib.property import *
from lib.property_repo import PropertyRepo

def test_get_all_properties(db_connection): 
    db_connection.seed("seeds/makers_bnb_database.sql") 
    repo = PropertyRepo(db_connection) 

    properties = repo.all() 

    assert properties == [
        Property(1,'The Ferns', '123 Wembley Downs', 'London', 'Haunted', 50, 1),
        Property(2,'The Laurels', '56 Secret Bay', 'Reykjavik', 'Cold', 30, 2),
        Property(3,'The Roses', '34 Sphinx Lane', 'Cairo', 'Warm', 60, 3),
        Property(4,'The Bananas', '1730 Clark St', 'Chicago', 'Windy', 65, 4),
        Property(5,'The Pines', '435 Melbourne Ave', 'Adelaide', 'Very Warm', 110, 5),
    ]


def test_get_single_property(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repo = PropertyRepo(db_connection)

    property = repo.find(3)
    
    assert property == Property(3,'The Roses', '34 Sphinx Lane', 'Cairo', 'Warm', 60, 3) 
    

def test_create_property(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repo = PropertyRepo(db_connection)

    repo.create(Property(6,'The Orange', '24 Cervantes St', 'Valencia', 'Very Warm', 90, 3))

    result = repo.all()
    assert result == [
        Property(1,'The Ferns', '123 Wembley Downs', 'London', 'Haunted', 50, 1),
        Property(2,'The Laurels', '56 Secret Bay', 'Reykjavik', 'Cold', 30, 2),
        Property(3,'The Roses', '34 Sphinx Lane', 'Cairo', 'Warm', 60, 3),
        Property(4,'The Bananas', '1730 Clark St', 'Chicago', 'Windy', 65, 4),
        Property(5,'The Pines', '435 Melbourne Ave', 'Adelaide', 'Very Warm', 110, 5),
        Property(6,'The Orange', '24 Cervantes St', 'Valencia', 'Very Warm', 90, 3)
    ]
    

def test_delete_property(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repo = PropertyRepo(db_connection)
    
    repo.delete(4) 

    result = repo.all()
    assert result == [
        Property(1,'The Ferns', '123 Wembley Downs', 'London', 'Haunted', 50, 1),
        Property(2,'The Laurels', '56 Secret Bay', 'Reykjavik', 'Cold', 30, 2),
        Property(3,'The Roses', '34 Sphinx Lane', 'Cairo', 'Warm', 60, 3),
        Property(5,'The Pines', '435 Melbourne Ave', 'Adelaide', 'Very Warm', 110, 5)
    ]
        
