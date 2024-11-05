from lib.users import Users
import pytest
# user class instantiates correctly with first name, surname, username and password
def test_users_instantiates_with_correct_attributes():
    users = Users(1, "Alan", "Turing", "Alan_Turing04", "Enigma")
    assert users.users_id == 1
    assert users.first_name == "Alan"
    assert users.surname == "Turing"
    assert users.username == "Alan_Turing04"
    assert users.password == "Enigma"



# User refuses non string as names, usernames and passwords
def test_users_rejects_non_string_inputs():
    with pytest.raises(Exception) as e:
         users = Users(1, "Alan", 98, "Alan_Turing04", "Enigma")
    assert str(e.value) == "String inputs only"

# Users can be compared for equality
def test_people_with_same_attributes_seen_as_equal():
    users1 = Users(1, "Alan", "Turing", "Alan_Turing04", "Enigma")
    users2 = Users(1, "Alan", "Turing", "Alan_Turing04", "Enigma")
    assert users1 == users2

# Users returned in the correct format
def test_users_returned_in_nice_format():
    users = Users(1, "Alan", "Turing", "Alan_Turing04", "Enigma")
    assert str(users) == "Users(1, Alan_Turing04)"
