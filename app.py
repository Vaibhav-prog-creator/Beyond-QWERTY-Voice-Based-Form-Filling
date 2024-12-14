from flask import Flask, render_template, request
import mysql.connector
import os

app = Flask(__name__)
app.secret_key = 'd1f3670c663dc08290c59bab47d05daa'  # Replace with the key you generated

db_config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "root",
    "database": "form"
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

        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            query = """
                INSERT INTO information (name, email, phone, age, education, course)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (name, email, phone, age, education, course))
            connection.commit()
            cursor.close()
            connection.close()
            return "Form submitted and data saved to the database successfully!"
        except mysql.connector.Error as err:
            return f"Error: {err}"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
