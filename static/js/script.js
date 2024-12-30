const form = document.getElementById('chatForm');
const userInput = document.getElementById('userInput');
const messagesDiv = document.getElementById('messages');

// Handle form submission
form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const userMessage = userInput.value; // Get user input
    addMessage(userMessage, 'user'); // Display user's message

    // Send the message to the server
    const response = await fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userMessage }),
    });

    const data = await response.json();
    addMessage(data.response, 'bot'); // Display bot's response

    userInput.value = ''; // Clear input field
});

// Function to display messages
function addMessage(message, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.textContent = message;
    messageDiv.className = sender; // Add class based on sender ('user' or 'bot')
    messagesDiv.appendChild(messageDiv);
    messagesDiv.scrollTop = messagesDiv.scrollHeight; // Scroll to the latest message
}
