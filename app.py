from flask import Flask, render_template, request
import mysql.connector
import os
from dotenv import load_dotenv  # Import dotenv to load environment variables

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'a4f5d9e7b2c0a8f4d1b7c3e9f1f0b6a2')  # Default secret key if not set in .env

# Fetch database credentials from environment variables
db_config = {
    "host": os.getenv("DB_HOST", "127.0.0.1"),  # Default to 127.0.0.1 if not set
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "root"),
    "database": os.getenv("DB_NAME", "form")
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        age = request.form.get("age")
        education = request.form.get("education")
        course = request.form.get("course")
        address = request.form.get("address")
        
        try:
            # Connect to the MySQL database
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            # Insert form data into the database
            query = """
                INSERT INTO information (name, email, phone, age, education, course, address)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (name, email, phone, age, education, course, address))

            # Commit changes to the database
            connection.commit()
            
            # Close the cursor and connection
            cursor.close()
            connection.close()

            return "Form submitted and data saved to the database successfully!"
        except mysql.connector.Error as err:
            return f"Error: {err}"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
