# SerenityChat - A Supportive Chatbot

SerenityChat is a chatbot built using **Dialogflow** and **Flask**. It provides supportive, empathetic responses to users, helping with mental health challenges and personal conversations.

## Features:
- Trained with various intents for mental health and personal assistance.
- Provides context-aware, empathetic chatbot responses.
- Easily deployable with Flask and Dialogflow integration.

## Prerequisites:
- Python 3.x
- Dialogflow account and project setup
- Google Cloud credentials (Dialogflow API key in JSON format)

## Installation:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/SerenityChat.git

2. Setup a virtual environment:
   ```bash
   python -m venv venv

3. Activate the virtual environment:
   ```bash
   venv\Scripts\activate

4. Install the required packages:
   ```bash
   pip install -r requirements.txt

5. Add the .JSON folder (shared with you in Google Drive) in the root directory of the project.

6. Set up the environment variable for Google Cloud credentials:
   ```bash
   $env:GOOGLE_APPLICATION_CREDENTIALS="path/to/your/dialogflow-key.json" (Paste the path of the .JSON folder)
   $env:DIALOGFLOW_PROJECT_ID="advanced-serenitychat-bxtb"
   ```
7. Run the Flask app:
   ```bash
   python app.py
   ```
