# Voice-Based Form Filling

This is a web application that allows users to fill out forms using their voice. The project uses Flask as the backend and integrates OpenAI’s Speech-to-Text API for processing voice input. The form data is saved to a MySQL database.

## Features
- **Voice Input**: Users can speak their responses to form fields.
- **Form Fields**: The form includes fields for name, email, phone, age, education, and course.
- **MySQL Integration**: The data is saved to a MySQL database for future reference.

## Setup

### Requirements:
- Python 3.x
- Flask
- MySQL
- OpenAI Speech-to-Text API

### Installation:
1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/Voice-Based-Form-Filling.git
    ```

2. Install the dependencies:
    ```bash
    cd Voice-Based-Form-Filling
    pip install -r requirements.txt
    ```

3. Set up the `.env` file with your MySQL credentials and OpenAI API key.

4. Run the Flask application:
    ```bash
    python app.py
    ```

### Usage:
- Access the form at `http://127.0.0.1:5000/`.
- Use the microphone button to fill out the form via voice input.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

