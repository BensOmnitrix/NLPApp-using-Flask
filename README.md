# Simple NLP App with Flask Authentication

## Overview
This project demonstrates the integration of natural language processing (NLP) functionality with a Flask-based login and registration system. The app fetches data from an external API, processes it using basic NLP techniques, and provides users with an interactive and secure platform.

## Features
- **User Authentication**:
  - Secure user registration.
  - User login/logout functionality with session management.
- **NLP Functionality**:
  - Fetches data from an external API.
  - Processes and displays the data with basic NLP operations (e.g., sentiment analysis, keyword extraction, or summarization).
- **Responsive UI**:
  - Simple and clean interface for seamless user interaction.

## Tech Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS
- **Database**: Used JSON for DB
- **API**: External NLP or text-based API for data fetching

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/BensOmnitrix/NLPApp-using-Flask.git
   cd NLPApp-using-Flask
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the environment variables:**
   - Create a `.env` file in the root directory.
   - Add the following variables:
     ```env
     FLASK_APP=app.py
     FLASK_ENV=development
     SECRET_KEY=your_secret_key
     API_KEY=your_api_key
     ```

5. **Run the application:**
   ```bash
   flask run
   ```

6. **Access the app:**
   Open your browser and navigate to `http://127.0.0.1:5000`.

## How It Works
1. **User Registration and Login**:
   - Users can register with a unique username and password.
   - Passwords are securely hashed using libraries like `werkzeug.security`.
   - Login credentials are verified, and users gain access to the NLP features upon successful login.

2. **NLP Functionality**:
   - Once logged in, users can interact with the NLP features.
   - Data is fetched from the external API (e.g. NLPCloud API).
   - The app processes the data and provides results such as:
     - Sentiment analysis.
     - NER (Named Entity Recognition)
     - Code Generation

## Future Enhancements
- Add role-based access control.
- Integrate advanced NLP models like Hugging Face transformers.
- Implement OAuth for third-party login options (e.g., Google, GitHub).
- Improve the UI/UX with a frontend framework (e.g., React or Vue).

## Contribution
Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.

---

**Developed with passion and determination.**

