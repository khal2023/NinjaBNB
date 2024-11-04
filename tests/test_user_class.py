from lib.user import User
import pytest
# user class instantiates correctly with first name, surname, username and password
def test_user_instantiates_with_correct_attributes():
    user = User(1, "Alan", "Turing", "Alan_Turing04", "Enigma")
    assert user.user_id == 1
    assert user.first_name == "Alan"
    assert user.surname == "Turing"
    assert user.username == "Alan_Turing04"
    assert user.password == "Enigma"



# User refuses non string as names, usernames and passwords
def test_user_rejects_non_string_inputs():
    with pytest.raises(Exception) as e:
         user = User(1, "Alan", 98, "Alan_Turing04", "Enigma")
    assert str(e.value) == "String inputs only"




# user class adds username and password if username is not already in the database