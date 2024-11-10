// script.js

// Generate a unique session ID once per conversation
let sessionId = generateSessionId();

function generateSessionId() {
    return Math.floor(Math.random() * 1000000000).toString();  // Unique session ID for the user
}

document.getElementById('chat-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const message = document.getElementById('message').value;
    const chatBox = document.getElementById('chat-box');

    // Add user's message
    chatBox.innerHTML += `
        <div class="message user-message">
            <img src="static/user.png" alt="User Profile Picture" class="profile-picture">
            ${message}
        </div>`;

    document.getElementById('message').value = '';

    // Show loading indicator
    chatBox.innerHTML += `
        <div class="message bot-message">
            <img src="static/bot.jpg" alt="Bot Profile Picture" class="profile-picture">
            <span id="loading">...</span>
        </div>`;

    chatBox.scrollTop = chatBox.scrollHeight;  // Scroll to the bottom

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: message, session_id: sessionId })  // Send session_id with each request
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        // Update the bot's response
        const loadingIndicator = document.getElementById('loading');
        loadingIndicator.parentNode.innerHTML = `
            <div class="message bot-message">
                <img src="static/bot.jpg" alt="Bot Profile Picture" class="profile-picture">
                ${data.response}
            </div>`;
        chatBox.scrollTop = chatBox.scrollHeight;  // Scroll to the bottom
    })
    .catch(error => {
        // Handle any errors
        chatBox.innerHTML += `
            <div class="message bot-message">
                <img src="static/bot.jpg" alt="Bot Profile Picture" class="profile-picture">
                Sorry, there was an error processing your request.
            </div>`;
        console.error('Error:', error);
        chatBox.scrollTop = chatBox.scrollHeight;  // Scroll to the bottom
    });
});
