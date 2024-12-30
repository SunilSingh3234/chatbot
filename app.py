from flask import Flask, request, jsonify, render_template # type: ignore
from flask_cors import CORS # type: ignore

app = Flask(__name__)
CORS(app)

# Rule-based chatbot response logic
def get_bot_response(user_input):
    responses = {
        "hello": "Hi there! How can I assist you?",
        "how are you?": "I'm just a bot, but I'm doing great! How about you?",
        "bye": "Goodbye! Have a great day!",
        "what is your name?":"I am a chat-bot , I don't have any specific name can you suggest me for my name?",
        "shree":"That's nice name",
        "hii":"hello, how can i help you?",
        "What is your name?": "I am your chatbot assistant.",
        "How are you?": "I'm just a program, but I'm here to help!",
        "What can you do?": "I can assist with coding, answer questions, and chat with you.",
        "Who created you?": "I was created by a team of developers at OpenAI.",
        "What is Python?": "Python is a high-level programming language used for general-purpose programming.",
        "What is your favorite color?": "I don't have eyes, but I imagine blue is quite calming.",
        "Can you solve math problems?": "Yes, I can help with math. Ask me a problem!",
        "What is AI?": "AI stands for Artificial Intelligence, the simulation of human intelligence in machines.",
        "Tell me a joke.": "Why do programmers prefer dark mode? Because light attracts bugs!",
        "How old are you?": "I exist outside of time, so I don't age!",
          # General questions
        "What is your name?": "I am your chatbot assistant.",
        "How are you?": "I'm doing great! How about you?",
        "What can you do?": "I can help with coding, answer questions, and keep you company.",
        # Programming-related
        "What is Python?": "Python is a popular programming language for various applications.",
        "What is a variable?": "A variable is a placeholder for storing data in a program.",
        "What is a function?": "A function is a reusable block of code that performs a specific task.",
        "What is HTML?": "HTML stands for HyperText Markup Language, used for creating web pages.",
        "What is an API?": "API stands for Application Programming Interface, which allows different applications to communicate.",
        # Math questions
        "What is 2+2?": "2+2 equals 4.",
        "What is the square root of 16?": "The square root of 16 is 4.",
        "What is pi?": "Pi is approximately 3.14159, a constant used in math.",
        # Science questions
        "What is gravity?": "Gravity is the force that attracts objects toward each other.",
        "What is the speed of light?": "The speed of light is approximately 299,792 kilometers per second.",
        "What is photosynthesis?": "Photosynthesis is how plants convert sunlight into energy.",
        # History questions
        "Who was Albert Einstein?": "Albert Einstein was a theoretical physicist known for the theory of relativity.",
        "What is the Great Wall of China?": "The Great Wall of China is a series of walls built for protection in ancient China.",
        "When was the internet invented?": "The internet was invented in the late 1960s.",
        # Fun questions
        "Tell me a joke.": "Why don't programmers like nature? Too many bugs!",
        "What is your favorite color?": "I don't have a favorite color, but I hear blue is popular.",
        "Can you sing?": "I can’t sing, but I can try to cheer you up!",
        # Technology questions
        "What is AI?": "AI stands for Artificial Intelligence, simulating human intelligence in machines.",
        "What is a database?": "A database is a collection of data stored for easy access and management.",
        "What is machine learning?": "Machine learning is a branch of AI that enables systems to learn from data.",
        # Cybersecurity questions
        "What is a firewall?": "A firewall is a security system that monitors and controls network traffic.",
        "What is phishing?": "Phishing is a scam where attackers trick people into providing sensitive information.",
        "What is encryption?": "Encryption is the process of encoding data to prevent unauthorized access.",
        # Random trivia
        "What is the capital of France?": "The capital of France is Paris.",
        "Who wrote 'Hamlet'?": "William Shakespeare wrote 'Hamlet.'",
        "What is the tallest mountain?": "Mount Everest is the tallest mountain.",
    }
    return responses.get(user_input.lower(), "Sorry, I don't understand that.")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = get_bot_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
