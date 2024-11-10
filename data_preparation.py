import json
import os
from google.cloud import dialogflow_v2 as dialogflow

# Set your Google Cloud project ID and language
PROJECT_ID = os.getenv('DIALOGFLOW_PROJECT_ID', 'advanced-serenitychat-bxtb')  # Use an environment variable
LANGUAGE_CODE = 'en'

# Define a function to send the message to Dialogflow
def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(request={"session": session, "query_input": query_input})
    return response.query_result.fulfillment_text

# Function to get the chatbot's response using Dialogflow
def get_response(user_input, user_id):
    session_id = f'session-{user_id}'  # Example of making session ID dynamic
    
    try:
        dialogflow_response = detect_intent_texts(PROJECT_ID, session_id, user_input, LANGUAGE_CODE)
    except Exception as e:
        return f"Sorry, I couldn't process your request: {str(e)}"

    return dialogflow_response
