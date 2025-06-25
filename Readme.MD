🤖 AI Chatbot
Welcome to the AI project! This application provides a seamless and interactive chat experience powered by the Google Gemini AI model. It features a lightweight Flask backend serving a responsive HTML/JavaScript frontend, where all AI interactions happen directly in your browser.

🌟 Features
Interactive Chat Interface: A clean, user-friendly UI for engaging conversations.

Gemini AI Integration: Directly leverages the powerful Gemini 2.0 Flash model for intelligent responses.

⚡ Streaming Responses: Experience real-time interaction as AI replies stream word-by-word.

Local API Key Storage: Your Gemini API key is conveniently and securely stored in your browser's localStorage.

Session Management: Easy "Save Key" and "Logout" options to manage your API key.

Dynamic Textarea: The input field intelligently auto-resizes to accommodate your messages.

📱 Responsive Design: Built with Tailwind CSS, ensuring a great experience on any device.

🛠️ Technologies Used
Frontend:

HTML5

CSS (Tailwind CSS)

JavaScript (Vanilla JS)

Backend:

Python (Flask)

AI Model:

Google Gemini

📁 Project Structure
.
├── app.py
├── config.py
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── static/css/style.css
├── templates/
    └── chat.html

🚀 Setup Instructions
Follow these steps to get your AI Chatbot up and running on your local machine.

1. Prerequisites
Python 3.x: Make sure Python is installed on your system.

Pip: Python's package installer, usually bundled with Python.

Gemini API Key: Obtain your personal API key from Google AI Studio or the Google Cloud Console. You will enter this key directly into the web application.

2. Backend Setup (Flask)
The Flask backend is primarily responsible for serving the chat.html file and handling session-related aspects (though the Gemini API calls are client-side).

Project Files:
Ensure you have app.py, config.py, requirements.txt, static, templates directory containing chat.html structured as shown in the Project Structure section above.

Create a Virtual Environment (Recommended):

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install Dependencies:
Install the necessary Python packages.

pip install -r requirements.txt


Create .env file:
Create a file named .env in the root directory (where app.py is) to manage environment variables.

FLASK_ENV=development
FLASK_APP=app.py
FLASK_RUN_PORT=5000 # Or 8000 if you prefer, matching config.py default
SECRET_KEY="your_super_strong_flask_session_key_here"


Run the Flask Application:
Navigate to your project's root directory in your terminal and execute:

flask run

The server will start, typically on http://127.0.0.1:8000/ (or the PORT you specified).


3. Frontend Setup (HTML/JavaScript)
The frontend is contained entirely within chat.html and interacts with the Gemini API.

File Location:
Ensure chat.html is located inside the templates/ directory relative to app.py.

Access the Application:
Open your web browser and navigate to the address where your Flask app is running (e.g., http://127.0.0.1:8000/).

👩‍💻 Usage
🔑 Enter your Gemini API Key:

Upon loading the page, you'll see a "Warning: Gemini AI Key is missing" message.

Input your Gemini API Key into the designated field in the header.

Click the "Save Key" button.

The status will update to "Gemini Key: Present", and the chat input will activate.

💬 Start Chatting:

Type your query into the "Ask me anything..." text area.

Press Enter (or click the send button \svg) to send your message.

Observe the AI's response stream dynamically into the chat.

🚪 Logout:

Click the "Logout" button to clear your API key from your browser's localStorage and reset the chat history. This is useful for security or if you wish to use a different key.

⚠️ Important Notes
API Key Security (Client-Side):
For simplicity in this project, the Gemini API key is stored directly in the browser's localStorage. This method is not recommended for production applications due to security risks. In a production environment, API keys should always be handled server-side to prevent exposure and misuse.

Streaming Implementation:
The streaming functionality relies on processing partial JSON responses from the Gemini API. While generally robust, network inconsistencies or unusual API response formats could potentially lead to minor display glitches.