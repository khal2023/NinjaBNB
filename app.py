import os
from flask import Flask, request, render_template, redirect, url_for, session
from lib.database_connection import get_flask_database_connection
from lib.property_repo import PropertyRepo
from lib.users_repo import UsersRepo
from lib.property import Property
from lib.booking_repo import BookingRepo
from lib.booking import Booking

# Create a new Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/ninjasunite')
def get_landing():
    return render_template('ninjas.html')

@app.route('/login', methods=['POST'])
def login_user():
    connection = get_flask_database_connection(app)
    user_repo = UsersRepo(connection)
    username = request.form['uname']
    password = request.form['psw']
    error_message = None
    if user_repo.validate_user(username, password):
        session['authenticated'] = True
        session['username'] = username
        return redirect("/home")
    else:
        error_message = "Incorrect username or password"
    return render_template("ninjas.html", error_message=error_message)
    
@app.route('/logout')
def logout_user():
    session.clear()
    return redirect('/nijasunite')

@app.route('/home')
def get_properties_on_home_page():
    if not session.get('authenticated'):
        return "Forbidden"
    else:
        connection = get_flask_database_connection(app)
        propertyrepo = PropertyRepo(connection)
        properties = propertyrepo.all()
        username = session.get('username')
        return render_template('index.html', properties=properties, username=username)
    
@app.route('/register')
def get_registration_page():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register_user():
    connection = get_flask_database_connection(app)
    user_repo = UsersRepo(connection)
    first_name = request.form['fname']
    last_name = request.form['lname']
    username = request.form['uname']
    password = request.form['psw']
    error_message = None
    try:
        user_repo.create(first_name, last_name, username, password)
        error_message = "Registration Successful! Please log in!"
        return render_template("ninjas.html", error_message=error_message)
    except Exception as e:
        error_message = str(e)
    return render_template("/register.html", error_message=error_message)

    
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

# Route to find specific details about specific property
@app.route("/home/<id>")
def get_property_from_id(id):
    if not session.get('authenticated'):
        return "Forbidden"
    else:
        connection = get_flask_database_connection(app)
        propertyrepo = PropertyRepo(connection)
        property = propertyrepo.find(id)
        username = session.get('username')
        return render_template('property.html', property=property, username=username)

@app.route('/successfulbooking')
def show_booking_success():
    return render_template("successfulbooking.html")

@app.route("/home/<id>", methods=['POST'])
def add_booking(id):
    if not session.get('authenticated'):
        return "Forbidden"
    else:
        connection = get_flask_database_connection(app)
        property_repo = PropertyRepo(connection)
        property = property_repo.find(id)
        booking_repo = BookingRepo(connection)
        user_repo = UsersRepo(connection)
        username = session.get('username')
        start = request.form['start_date']
        end = request.form['end_date']
        error_message = None
        try:
            booking_repo.make_booking(username, property.name, start, end)
            return redirect("/successfulbooking")
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
    




        # connection = get_flask_database_connection(app)
        # property_repo = PropertyRepo(connection)
        # property = property_repo.find(id)
        # booking_repo = BookingRepo(connection)
        # user_repo = UsersRepo(connection)
        # username = request.form['username']
        # password = request.form['user_password']
        # start = request.form['start_date']
        # end = request.form['end_date']
        # error_message = None
        # try:
        #     if user_repo.validate_user(username, password):
        #         booking_repo.make_booking(username, property.name, start, end)
        #         return redirect("/successfulbooking")
        #     else:
        #         error_message = "Invalid username or password"
        # except Exception as e:
        #     error_message = str(e)
        # return render_template("property.html", property=property, error_message=error_message)
