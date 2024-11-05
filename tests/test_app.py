from playwright.sync_api import Page, expect

# Tests for your routes go here



# Get properties from database
def test_get_existing_properties(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    page.goto("http://{test_web_address}/listproperties")
    


# Post user data to database on registration

# Post property data to database


"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")

    # We look at the <p> tag
    p_tag = page.locator("p")

    # We assert that it has the text "This is the homepage."
    expect(p_tag).to_have_text("This is the homepage.")