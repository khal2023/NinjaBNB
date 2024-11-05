from lib.person_repo import PersonRepo
from lib.person import Person


# find person from db based on person_id
def test_find_person(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repo = PersonRepo(db_connection)
    assert repo.find(1) == Person(1, 'Khalid', 'Ham', 'KHam', None)

def test_find_username_in_db(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repo = PersonRepo(db_connection)
    assert repo.username_in_db("KHam") == True
    assert repo.username_in_db("MarkAnthony") == False

# # create person in db if they pass username and password validation tests
def test_create_person(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repo = PersonRepo(db_connection)
    repo.create("Hunor", "Tamas", "C0deMaster", "Apple24!")
    assert repo.username_in_db("C0deMaster") == True

def test_create_refuses_incorrect_password(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repo = PersonRepo(db_connection)
    repo.create("Hunor", "Tamas", "C0deMaster", "Apple!")
    assert repo.username_in_db("C0deMaster") == False



# remove person from db based on selection criteria 
