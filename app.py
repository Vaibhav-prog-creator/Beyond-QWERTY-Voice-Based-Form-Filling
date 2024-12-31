from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import os
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'a4f5d9e7b2c0a8f4d1b7c3e9f1f0b6a2')

# Database configuration (Updated with provided details)
db_config = {
    "host": "sql12.freesqldatabase.com",  # Updated host
    "user": "sql12754845",  # Updated user
    "password": "LWrgRcrnVZ",  # Updated password
    "database": "sql12754845",  # Updated database name
    "port": 3306  # Port for the MySQL server
}

# Default Route - Sign Up Page
@app.route("/", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        
        # Hash the password
        hashed_password = generate_password_hash(password)

        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            
            # Check if the user already exists
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            user = cursor.fetchone()
            
            if user:
                return "User already exists!"
            
            # Insert new user
            query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
            cursor.execute(query, (username, email, hashed_password))
            connection.commit()
            
            cursor.close()
            connection.close()
            
            # Redirect to Sign In page after successful sign up
            return redirect(url_for('signin'))  # Make sure to use 'signin' here
        
        except mysql.connector.Error as err:
            return f"Error: {err}"
    
    return render_template("signup.html")


# Sign In Page
@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            
            # Verify user credentials
            query = "SELECT * FROM users WHERE email = %s"
            cursor.execute(query, (email,))
            user = cursor.fetchone()  # Fetch the user row
            
            cursor.close()
            connection.close()

            # If user exists and password is correct
            if user and check_password_hash(user[3], password):  # user[3] contains the hashed password
                session['user'] = user[1]  # Store the username in the session
                return redirect(url_for('index'))  # Redirect to the main page
            
            return "Invalid credentials!"  # Show error if the credentials are incorrect
        
        except mysql.connector.Error as err:
            return f"Error: {err}"
    
    return render_template("signin.html")


# Main Page (Form Page)
@app.route("/main", methods=["GET", "POST"])
def index():
    if 'user' not in session:
        return redirect(url_for('signin'))
    
    if request.method == "POST":
        # Get form data including the new fields
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        age = request.form.get("age")
        education = request.form.get("education")
        course = request.form.get("course")
        address = request.form.get("address")
        percentage_12th = request.form.get("percentage_12th")  # New field
        percentage_10th = request.form.get("percentage_10th")  # New field
        
        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            
            # Insert form data including the new fields into the database
            query = """
                INSERT INTO form_data (name, email, phone, age, education, course, address, percentage_12th, percentage_10th, submitted_by)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (name, email, phone, age, education, course, address, percentage_12th, percentage_10th, session['user']))
            connection.commit()
            
            cursor.close()
            connection.close()
            
            return "Form submitted successfully!"
        
        except mysql.connector.Error as err:
            return f"Error: {err}"
    
    return render_template("index.html", user=session['user'])


# Logout
@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for('signin'))


if __name__ == "__main__":
    app.run(debug=True)
