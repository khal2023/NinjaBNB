# from playwright.sync_api import Page, expect
# from lib.property import Property

# # HTTP Tests
# def test_http_get_users(web_client, db_connection):
#     db_connection.seed("seeds/makers_bnb_database.sql")
#     response = web_client.get('/users')
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == 'KHam, BShariffali, LPaine, ATobarra, JONeill' 

# def test_http_post_adds_a_user(web_client, db_connection):
#     db_connection.seed("seeds/makers_bnb_database.sql")
#     post_response = web_client.post('/users', data={
#         'first_name': 'Alan',
#         'surname': 'Turing',
#         'username': 'Alan_turing04',
#         'user_password': 'EnigmaAlan!'
#     })
#     assert post_response.status_code == 200
#     response = web_client.get('/users')
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == 'KHam, BShariffali, LPaine, ATobarra, JONeill, Alan_turing04'

# def test_http_get_single_user(web_client, db_connection):
#     db_connection.seed("seeds/makers_bnb_database.sql")
#     response = web_client.get('/users/ATobarra')
#     response.status_code == 200
#     response.data.decode('utf-8') == "User(4, 'Alberto', 'Tobarra', 'ATobarra', None)"

# def test_http_get_existing_properties(web_client, db_connection):
#     db_connection.seed("seeds/makers_bnb_database.sql")
#     response = web_client.get('/properties')
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == "The Ferns, The Laurels, The Roses, The Bananas, The Pines"

# def test_http_get_existing_property_from_id(web_client, db_connection):
#     db_connection.seed("seeds/makers_bnb_database.sql")
#     response = web_client.get('/properties/1')
#     assert response.status_code == 200 
#     assert response.data.decode('utf-8') == "Property(1,'The Ferns', '123 Wembley Downs', 'London', 'Haunted', 50, 1)"

# def test_http_post_property(web_client, db_connection):
#     db_connection.seed("seeds/makers_bnb_database.sql")
#     post_response = web_client.post('/properties', data={
#         "property_name": "The Oaks",
#         "street_address": "143 Alan Lane",
#         "city": "Megalopolis",
#         "property_description": "Very large",
#         "price_per_night": 145,
#         "host_id": 2
#         })
#     response = web_client.get('/properties')
#     assert post_response.status_code == 200
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == "The Ferns, The Laurels, The Roses, The Bananas, The Pines, The Oaks"


# # HTML Tests
# def test_get_existing_properties(page, test_web_address, db_connection):
#     page.set_default_timeout(1000)
#     db_connection.seed("seeds/makers_bnb_database.sql")
#     page.goto(f"http://{test_web_address}/home")
#     div_tags = page.locator("div")
#     expected_properties = [
#         "The Ferns, London: Haunted",
#         "The Laurels, Reykjavik: Cold",
#         "The Roses, Cairo: Warm",
#         "The Bananas, Chicago: Windy", 
#         "The Pines, Adelaide: Very Warm"
#     ]
#     for i, text in enumerate(expected_properties):
#         expect(div_tags.nth(i)).to_have_text(text)

# def test_log_in_recognises_existing_users(page, test_web_address, db_connection):
#     page.set_default_timeout(1000)
#     db_connection.seed("seeds/makers_bnb_database.sql")
#     page.goto(f"http://{test_web_address}/home")
#     page.click("text=Log in")
#     page.fill("input[name=username]", "Kham")
#     page.fill("input[name=password]", "Python24")
#     h1_tags = page.locator('h1')
#     expect(h1_tags).to_have_text("Welcome, Khalid Ham!")

# def test_post_registers_new_user(page, test_web_address, db_connection):
#     page.set_default_timeout(1000)
#     db_connection.seed("seeds/makers_bnb_database.sql")
#     page.goto(f"http://{test_web_address}/home")
#     page.click("text=Register")
#     page.fill("input[name=first_name]", "Alan")
#     page.fill("input[name=surname]", "Turing")
#     page.fill("input[name=username]", "Alan_turing04")
#     page.fill("input[name=password]", "EnigmaAlan!")
#     h1_tags = page.locator('h1')
#     expect(h1_tags).to_have_text("Welcome, Alan Turing!")







# Post property data to database


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