from lib.property import *
from lib.property_repo import PropertyRepo

def test_get_all_properties(db_connection): 
    db_connection.seed("seeds/makers_bnb_database.sql") 
    repo = PropertyRepo(db_connection) 

    properties = repo.all() 

    assert properties == [
        Property('The Ferns', '123 Wembley Downs', 'London', 'Haunted', 50, 1),
        Property('The Laurels', '56 Secret Bay', 'Reykjavik', 'Cold', 30, 2),
        Property('The Roses', '34 Sphinx Lane', 'Cairo', 'Warm', 60, 3),
        Property('The Bananas', '1730 Clark St', 'Chicago', 'Windy', 65, 4),
        Property('The Pines', '435 Melbourne Ave', 'Adelaide', 'Very Warm', 110, 5),
    ]


def test_get_single_user(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repo = PropertyRepo(db_connection)

    user = repo.find(3)
    
    assert user == Property(3,'Lou', 'Paine', 'LPaine', 'Fortran90') 
    

def test_create_user(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repo = PropertyRepo(db_connection)

    repo.create(Property(None,'The Orange', '24 Cervantes St', 'Valencia', 'Very Warm', 90, 6))

    result = repo.all()
    assert result == [
        Property('The Ferns', '123 Wembley Downs', 'London', 'Haunted', 50, 1),
        Property('The Laurels', '56 Secret Bay', 'Reykjavik', 'Cold', 30, 2),
        Property('The Roses', '34 Sphinx Lane', 'Cairo', 'Warm', 60, 3),
        Property('The Bananas', '1730 Clark St', 'Chicago', 'Windy', 65, 4),
        Property('The Pines', '435 Melbourne Ave', 'Adelaide', 'Very Warm', 110, 5),
        Property('The Orange', '24 Cervantes St', 'Valencia', 'Very Warm', 90, 6)
    ]
    

def test_delete_user(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repo = PropertyRepo(db_connection)
    
    repo.delete(4) 

    result = repo.all()
    assert result == [
        Property('The Ferns', '123 Wembley Downs', 'London', 'Haunted', 50, 1),
        Property('The Laurels', '56 Secret Bay', 'Reykjavik', 'Cold', 30, 2),
        Property('The Roses', '34 Sphinx Lane', 'Cairo', 'Warm', 60, 3),      
    ]
