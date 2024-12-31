# Admission Form Filling Application

This project is an educational **form-filling application** that allows users to fill out forms using **voice input**, aiming to provide a seamless and user-friendly experience. The app features a modern, visually appealing front end and a robust backend using Python with Flask.

---

## Features

- **Voice Input Integration**: Users can fill forms using speech, leveraging OpenAI's Speech-to-Text API.
- **Database Support**: Data is stored in a MySQL database for efficient management.
- **Modern Frontend**: A visually appealing interface designed for a smooth user experience.
- **Scalable Backend**: Built with Flask, ensuring reliability and scalability.
- **Cross-Browser Compatibility**: Works seamlessly on modern browsers.

---

## Tech Stack

### Frontend
- **HTML5 / CSS3 / JavaScript**
- Bootstrap for responsive design

### Backend
- **Python** with Flask framework
- OpenAI's Speech-to-Text API for voice input processing

### Database
- **MySQL**: Data stored in the `education_form` database, specifically in the `registrations` table

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
   ```

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
   DATABASE_URI=mysql+pymysql://username:password@localhost/education_form
   OPENAI_API_KEY=your_openai_api_key
   ```

5. Run the application:
   ```bash
   flask run
   ```

6. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

---

## Usage

1. Open the application in your browser.
2. Use the voice input feature to fill out form fields.
3. Submit the form to save data to the database.

---

## Screenshots
Following are screenshots
 Following are screenshots:

![Sign up](screenshots/screenshot1.png)
![Sign in](screenshots/screenshot2.png)
![main page](screenshots/screenshot3.png)
---
 

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

For any inquiries or support, feel free to contact:

- **Name**: Vaibhav Sunil Shimpi
- **GitHub**: [Vaibhav-prog-creator](https://github.com/Vaibhav-prog-creator)

---
