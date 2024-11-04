from lib.person import Person
import pytest
# user class instantiates correctly with first name, surname, username and password
def test_person_instantiates_with_correct_attributes():
    person = Person(1, "Alan", "Turing", "Alan_Turing04", "Enigma")
    assert person.person_id == 1
    assert person.first_name == "Alan"
    assert person.surname == "Turing"
    assert person.username == "Alan_Turing04"
    assert person.password == "Enigma"



# User refuses non string as names, usernames and passwords
def test_person_rejects_non_string_inputs():
    with pytest.raises(Exception) as e:
         person = Person(1, "Alan", 98, "Alan_Turing04", "Enigma")
    assert str(e.value) == "String inputs only"

# Users can be compared for equality
def test_people_with_same_attributes_seen_as_equal():
    person1 = Person(1, "Alan", "Turing", "Alan_Turing04", "Enigma")
    person2 = Person(1, "Alan", "Turing", "Alan_Turing04", "Enigma")
    assert person1 == person2

# Users returned in the correct format
def test_person_returned_in_nice_format():
    person = Person(1, "Alan", "Turing", "Alan_Turing04", "Enigma")
    assert str(person) == "Person(1, Alan_Turing04)"