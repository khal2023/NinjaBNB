# from playwright.sync_api import Page, expect
# from lib.property import Property

# # Get properties from database
# def test_get_existing_properties(page, test_web_address, db_connection):
#     db_connection.seed("seeds/makers_bnb_database.sql")
#     page.goto(f"http://{test_web_address}/home")
#     div_tags = page.locator("div")
#     expected_properties = [
#         "The Ferns, London: Haunted"
#         "The Laurels, Reykjavik: Cold",
#         "The Roses, Cairo: Warm",
#         "The Bananas, Chicago: Windy", 
#         "The Pines, Adelaide: Very Warm"
#     ]
#     for i, text in enumerate(expected_properties):
#         expect(div_tags.nth(i)).to_have_text(text)

# def test_log_in_recognises_existing_users(page, test_web_address, db_connection):
#     db_connection.seed("seeds/makers_bnb_database.sql")
#     page.goto(f"http://{test_web_address}/home")
#     page.click("text=Log in")
#     page.fill("input[name=username]", "Kham")
#     page.fill("input[name=password]", "Python24")
#     h1_tags = page.locator('h1')
#     expect(h1_tags).to_have_text("Welcome, Khalid Ham!")



# def test_post_registers_new_user(page, test_web_address, db_connection):
#     db_connection.seed("seeds/makers_bnb_database.sql")
#     page.goto(f"http://{test_web_address}/home")
#     page.click("text=Register")
#     page.fill("input[name=first_name]", "Alan")
#     page.fill("input[name=surname]", "Turing")
#     page.fill("input[name=username]", "Alan_turing04")
#     page.fill("input[name=password]", "EnigmaAlan!")
#     h1_tags = page.locator('h1')
#     expect(h1_tags).to_have_text("Welcome, Alan Turing!")

# # Post property data to database


# """
# We can render the index page
# """
# def test_get_index(page, test_web_address):
#     # We load a virtual browser and navigate to the /index page
#     page.goto(f"http://{test_web_address}/index")

#     # We look at the <p> tag
#     p_tag = page.locator("p")

#     # We assert that it has the text "This is the homepage."
#     expect(p_tag).to_have_text("This is the homepage.")