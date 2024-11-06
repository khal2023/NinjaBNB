from lib.users_repo import UsersRepo
from lib.users import Users


# find users from db based on users_id
def test_find_users(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repo = UsersRepo(db_connection)
    assert repo.find(1) == Users(1, 'Khalid', 'Ham', 'KHam', None)

def test_find_username_in_db(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repo = UsersRepo(db_connection)
    assert repo.username_in_db("KHam") == True
    assert repo.username_in_db("MarkAnthony") == False

# # create users in db if they pass username and password validation tests
def test_create_users(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repo = UsersRepo(db_connection)
    repo.create("Hunor", "Tamas", "C0deMaster", "Apple24!")
    assert repo.username_in_db("C0deMaster") == True

def test_create_refuses_incorrect_password(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repo = UsersRepo(db_connection)
    repo.create("Hunor", "Tamas", "C0deMaster", "Apple!")
    assert repo.username_in_db("C0deMaster") == False

def test_validate_user(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repo = UsersRepo(db_connection)
    assert repo.validate_user("KHam", "Python24") == True


# remove users from db based on selection criteria 
