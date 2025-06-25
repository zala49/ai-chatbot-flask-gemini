import os
from dotenv import load_dotenv

load_dotenv()

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    jsonify,
    flash,
)
from config import config_by_name

app = Flask(__name__)

FLASK_ENV = os.environ.get("FLASK_ENV", "development")
config_object = config_by_name.get(FLASK_ENV, config_by_name["default"])()
app.config.from_object(config_object)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/")
def chat():
    """
    Renders the chatbot interface page.
    The Gemini API key is now passed from the session to the frontend.
    """
    gemini_api_key = session.get("gemini_api_key", "")
    return render_template("chat.html", gemini_api_key=gemini_api_key)


@app.route("/set_gemini_key", methods=["POST"])
def set_gemini_key():
    """
    Endpoint to receive and store the Gemini API key in the session.
    """
    data = request.get_json()
    gemini_api_key = data.get("apiKey")

    if gemini_api_key:
        session["gemini_api_key"] = gemini_api_key
        return jsonify({"status": "success", "message": "Gemini AI Key saved."})
    else:
        return (
            jsonify({"status": "error", "message": "No Gemini AI Key provided."}),
            400,
        )


@app.route("/generate_response", methods=["POST"])
def generate_response():
    """
    Endpoint to call the Gemini API and get AI responses.
    The Gemini API key is now passed from the session to the frontend.
    """
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    ai_response_text = (
        f"AI received: '{user_message}' (Frontend is handling Gemini API call directly)"
    )

    return jsonify({"response": ai_response_text})


@app.route("/logout")
def logout():
    """Logs out the user by clearing the session."""
    session.pop("gemini_api_key", None)
    flash("You have been logged out.", "info")
    return redirect(url_for("chat"))


if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])
