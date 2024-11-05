import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route("/home")
def get_home_with_available_properties():
    connection = get_flask_database_connection(app)
    repository = PropertyRepo(connection)
    properties = repository.all()
    return render_template("index.html", properties = properties)

# @app.route("/register", methods=['POST'])
# def register_new_user
# #     connection = get_flask_database_connection()

# Route that registers user and redirects them to login page

# Route that logs user in and redirects them to booking page






# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
