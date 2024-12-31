# Admission Form Filling Application

This project is an educational **form-filling application** that allows users to fill out forms using **voice input**, aiming to provide a seamless and user-friendly experience. The app features a modern, visually appealing front end and a robust backend using Python with Flask.

---
## project Deployment 

You can access the live deployed version of the project here:
https://beyond-qwerty-voice-based-form-filling-1.onrender.com

## Features

- **Voice Input Integration**: Users can fill forms using speech, leveraging OpenAI's Speech-to-Text API and **Web Speech API** for voice recognition.
- **Database Support**: Data is stored in a MySQL database for efficient management.
- **Modern Frontend**: A visually appealing interface designed for a smooth user experience.
- **Scalable Backend**: Built with Flask, ensuring reliability and scalability.
- **Cross-Browser Compatibility**: Works seamlessly on modern browsers.

---

## Tech Stack

### Frontend
- **HTML5 / CSS3 / JavaScript**
- Bootstrap for responsive design
- **Web Speech API** for voice input processing

### Backend
- **Python** with Flask framework
- Web Speech-to-Text API for voice input processing

### Database
- **MySQL**: Data stored in the `sql12754845` database, specifically in the `form_data` table

### Other Tools and Libraries
- Flask-SQLAlchemy for database interaction
- Flask-Migrate for database migrations
- WTForms for form handling

---

## Installation

### Prerequisites

- Python 3.9+
- MySQL Database
- pip (Python package installer)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Vaibhav-prog-creator/Admission_form_filling.git
   cd Admission_form_filling
Install the required dependencies:

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:
   - Create a database named `sql12754845`.
   - Ensure the `form_data` table is properly set up using migrations or SQL scripts provided.

4. Create a `.env` file for sensitive configurations:
   ```env
   FLASK_APP=app.py
   FLASK_ENV=development
   SECRET_KEY=a4f5d9e7b2c0a8f4d1b7c3e9f1f0b6a2

   DB_HOST=sql12.freesqldatabase.com
   DB_USER=sql12754845
   DB_PASSWORD=LWrgRcrnVZ
   DB_NAME=sql12754845
   DATABASE_URL=mysql+pymysql://sql12754845:LWrgRcrnVZ@sql12.freesqldatabase.com:3306/sql12754845
   ```

5. Run the application:
   ```bash
   flask run
   ```

arduino
Copy code
http://127.0.0.1:5000
Usage
Open the application in your browser.
Use the voice input feature to fill out form fields, leveraging the Web Speech API.
Submit the form to save data to the database.
Screenshots
Following are screenshots:

![Sign up](screenshots/screenshot1.png)
![Sign in](screenshots/screenshot2.png)
![main page](screenshots/screenshot3.png)
---
 

## License

This project is licensed under the [MIT License](LICENSE).


 ## Certificates

HackerRank Python Certificate https://www.hackerrank.com/certificates/2759fb091576

HackerRank SQL Certificate    https://www.hackerrank.com/certificates/a216c46fb0dd
 


## Contact
For any inquiries or support, feel free to contact:

Name: Vaibhav Sunil Shimpi
GitHub: Vaibhav-prog-creator



For any inquiries or support, feel free to contact:

- **Name**: Vaibhav Sunil Shimpi
- **GitHub**: [Vaibhav-prog-creator](https://github.com/Vaibhav-prog-creator)

---
