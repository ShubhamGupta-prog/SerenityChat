# app.py

from flask import Flask, request, jsonify, render_template
from google.cloud import dialogflow_v2 as dialogflow
import os

app = Flask(__name__)

# Set your Google Cloud project ID and language from environment variables
PROJECT_ID = os.getenv('DIALOGFLOW_PROJECT_ID', 'advanced-serenitychat-bxtb')
LANGUAGE_CODE = 'en'

# Define a function to send the message to Dialogflow
def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(request={"session": session, "query_input": query_input})
    return response.query_result.fulfillment_text

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    session_id = request.json.get('session_id')  # Use session_id from the frontend

    try:
        dialogflow_response = detect_intent_texts(PROJECT_ID, session_id, user_input, LANGUAGE_CODE)
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'response': 'Sorry, something went wrong. Please try again.'}), 500

    return jsonify({'response': dialogflow_response})

if __name__ == '__main__':
    app.run(debug=True)
