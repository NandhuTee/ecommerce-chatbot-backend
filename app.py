from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # To allow frontend (like Vite React) to access backend
@app.route("/api/chat/message", methods=["POST"])

def chatbot_reply():
    user_input = request.json.get("message", "").lower()
    response = "❓ Sorry, I didn’t understand that."

    if "book" in user_input:
        response = "✅ Cylinder booked! How would you like to pay? (Cash / GPay)"
    elif "cash" in user_input or "gpay" in user_input:
        response = "💰 Payment recorded. Thank you! Have a nice day 😊"
    elif "hello" in user_input or "hi" in user_input:
        response = "Hi there! I can help you book a cylinder."

    return jsonify({"reply": response})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
