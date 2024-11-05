from lib.person_repo import PersonRepo
from lib.person import Person


# find person from db based on person
def test_find_person(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repo = PersonRepo(db_connection)
    assert repo.find(1) == 'Person(1, KHam)'
    
    # Person(1, 'Khalid', 'Ham', 'KHam', 'Python24')
# create person in db if they pass password validation tests
# def test_create_person_in_db(db_connection)
# create person in db if they pass username validation tests
# remove person from db based on selection criteria 
