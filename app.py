import os
from flask import Flask, request, render_template, redirect, url_for
from lib.database_connection import get_flask_database_connection
from lib.property_repo import PropertyRepo
from lib.users_repo import UsersRepo
from lib.property import Property
from lib.booking_repo import BookingRepo
from lib.booking import Booking

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

# Route to test user can be added
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

# Route to home and list all properties
@app.route('/home')
def get_properties_on_home_page():
    connection = get_flask_database_connection(app)
    propertyrepo = PropertyRepo(connection)
    properties = propertyrepo.all()
    return render_template('index.html', properties=properties)


# Route to find specific details about specific property
@app.route("/home/<id>")
def get_property_from_id(id):
    connection = get_flask_database_connection(app)
    propertyrepo = PropertyRepo(connection)
    property = propertyrepo.find(id)
    return render_template('property.html', property=property)

@app.route('/successfulbooking')
def show_booking_success():
    return render_template("successfulbooking.html")

@app.route("/home/<id>", methods=['POST'])
def add_booking(id):
    connection = get_flask_database_connection(app)
    property_repo = PropertyRepo(connection)
    property = property_repo.find(id)
    booking_repo = BookingRepo(connection)
    user_repo = UsersRepo(connection)
    username = request.form['username']
    password = request.form['user_password']
    start = request.form['start_date']
    end = request.form['end_date']
    error_message = None
    try:
        if user_repo.validate_user(username, password):
            booking_repo.make_booking(username, property.name, start, end)
            return redirect("/successfulbooking")
        else:
            error_message = "Invalid username or password"
    except Exception as e:
        error_message = str(e)
    return render_template("property.html", property=property, error_message=error_message)

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

# HTML Routes


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(
        debug=True,
        port=int(os.environ.get('PORT', 5001))
    )
    
