from lib.property import *

def test_property_construction():
    property = Property(2, "testname", "street_address", "London", "property description", 150, 1)

    assert property.id == 2
    assert property.name == "testname"
    assert property.street_address == "street_address"
    assert property.city == "London"
    assert property.property_description == "property description"
    assert property.price_per_night == 150
    assert property.host_id == 1
    
def test_property_are_equal():
    property1 = Property(2, "testname", "street_address", "London", "property description", 150, 1)
    property2 = Property(2, "testname", "street_address", "London", "property description", 150, 1)
    
    assert property1 == property2

def test_property_format_nicely():
    property = Property(2, "testname", "street_address", "London", "property description", 150, 1)

    assert str(property) == 'Property(2, testname, street_address, London, property description, 150, 1)'
