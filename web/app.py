import os
import psycopg
from flask import Flask, request, render_template, redirect, url_for
from lib.database_connection import get_flask_database_connection
# from markupsafe import escape
from lib.property_repo import PropertyRepo
from lib.users_repo import UsersRepo

# Function that constructs an URL for the database

# def get_database_url():
#     if os.environ.get("APP_ENV") == "PRODUCTION":
#         password = os.environ.get("POSTGRES_PASSWORD")
#         hostname = os.environ.get("POSTGRES_HOSTNAME")
#         return f"postgres://postgres:{password}@{hostname}:5432/postgres"
#     else:
#         return "postgres://localhost:5432/postgres"

# # Function that sets up the database with the right table

# def setup_database(url):
#     connection = psycopg.connect(url)
#     cursor = connection.cursor()
#     cursor.execute("CREATE TABLE IF NOT EXISTS messages (message TEXT);")
#     connection.commit()
    
# POSTGRES_URL = get_database_url()
# setup_database(POSTGRES_URL)

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/users', methods = ['GET'])
def http_get_users():
    connection = get_flask_database_connection(app)
    usersrepo = UsersRepo(connection)
    users = usersrepo.list_all_users()
    usernames = []
    for user in users:
        usernames.append(user.username)
    return (", ").join(usernames)

@app.route("/home")
def get_home_with_available_properties():
    connection = get_flask_database_connection(app)
    repository = PropertyRepo(connection)
    properties = repository.all()
    return render_template("index.html", properties = properties)

@app.route('/bookings', methods = ['POST'])
def booking():
    connection = get_flask_database_connection(app)
    repository = PropertyRepo(connection)
    properties = repository.all()
    return render_template("Booking.html")

# Route that log in user and redirect them to login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if valid_users(username, password):
            return redirect(url_for('Booking'))
        else:
            return "Invalid username or password"
    
    return render_template('Login.html')


# Route that registers user and redirects them to login page
@app.route("/register", methods=['POST'])
def register_new_user():
    if request.method == 'POST':
        first_name = request.form [first_name]
        surname = request.form [surname]
        username = request.form [username]
        password = request.form [password]

        if valid_users(first_name, surname, username, password):
            return redirect(url_for('index'))
        else:
            return "Invalid username or password"




# # Route to list all properties
# @app.route('/all', methods = ['GET'])
# def get_all_properties_from_users():
#     return redirect(url_for(''))
    
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
    
    # if os.environ.get("APP_ENV") == "PRODUCTION":
    #     app.run(port=5000, host='0.0.0.0')
    
    # else:
    app.run(
        debug=True,
        port=int(os.environ.get('PORT', 5001)),
        host="0.0.0.0"
    )
    
