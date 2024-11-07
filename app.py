import os
from flask import Flask, request, render_template, redirect, url_for
from lib.database_connection import get_flask_database_connection
from lib.property_repo import PropertyRepo
from lib.users_repo import UsersRepo
from lib.property import Property

# Create a new Flask app
app = Flask(__name__)

# Route to get all users
@app.route('/users', methods = ['GET'])
def http_get_users():
    connection = get_flask_database_connection(app)
    usersrepo = UsersRepo(connection)
    users = usersrepo.list_all_users()
    usernames = []
    for user in users:
        usernames.append(user.username)
    return (", ").join(usernames)

# Route to find a property by specific properties
@app.route("/home")
def get_home_with_available_properties():
    connection = get_flask_database_connection(app)
    repository = PropertyRepo(connection)
    properties = repository.all()
    return render_template("index.html", properties = properties)

# Route to show all properties booked
@app.route('/bookings', methods = ['POST'])
def booking():
    connection = get_flask_database_connection(app)
    repository = PropertyRepo(connection)
    properties = repository.all()
    return render_template("Booking.html")

# Route that log in user and redirect them to login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form['username']
    password = request.form['password']
        
        # if valid_users(username, password):
        #     return redirect(url_for('Booking'))
        # else:
        #     return "Invalid username or password"
    
    return render_template('Login.html')


# Route that registers user and redirects them to login page
@app.route("/users", methods=['POST'])
def register_new_user():
    first_name = request.form['first_name']
    surname = request.form['surname']
    username = request.form['username']
    password = request.form['user_password']
    connection = get_flask_database_connection(app)
    usersrepo = UsersRepo(connection)
    usersrepo.create(first_name, surname, username, password)
    return "user added"
        

        # if valid_users(first_name, surname, username, password):
        #     return redirect(url_for('index'))
        # else:
        # return "Invalid username or password"


# Route to list all properties
@app.route('/properties', methods = ['GET'])
def http_get_existing_properties():
    connection = get_flask_database_connection(app)
    propertyrepo = PropertyRepo(connection)
    properties = propertyrepo.all()
    properties_list = []
    for property in properties:
        properties_list.append(property.name)
    return (", ").join(properties_list)

# Route to find a property by id
@app.route('/properties/<int:id>', methods = ['GET'])
def http_get_existing_property_from_id(id):
    connection = get_flask_database_connection(app)
    propertyrepo = PropertyRepo(connection)
    return str(propertyrepo.find(id))
    return properties.name

# Route to create a new property and post it in existing properties
@app.route('/properties', methods = ['POST'])
def http_post_property():
    
    property_name = request.form['property_name']
    street_address = request.form['street_address']
    city = request.form['city']
    property_description = request.form['property_description']
    price_per_night = request.form['price_per_night']
    host_id = request.form['host_id']
    
    property = Property(None, property_name, street_address, city, property_description, price_per_night, host_id)
    
    connection = get_flask_database_connection(app)
    propertyrepo = PropertyRepo(connection)
    propertyrepo.create(property)
    
    existing_properties = propertyrepo.all()
    new_properties_list = []
    for property in existing_properties:
        new_properties_list.append(property.name)
    return (", ").join(new_properties_list)
    


# # Route to find a property
# @app.route('/find', methods = ['GET'])
# def find_property_from_user():
#     return redirect(url_for(''))

# # Route to create a new property
# @app.route('/create', methods = ['POST'])
# def create_new_property_for_a_user():
#     list_properties = request.form
#     return redirect(url_for(''))
    
# # Route to remove a property
# @app.route('/delete', methods = ['GET'])
# def delete_any_property():
#     return redirect(url_for(''))

# @app.route('/index', methods=['GET'])
# def get_index():
#     return render_template('index.html')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(
        debug=True,
        port=int(os.environ.get('PORT', 5001)),
        host="0.0.0.0"
    )
    
