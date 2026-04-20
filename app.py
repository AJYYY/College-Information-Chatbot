import json
import random
from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = Flask(__name__)


with open('intents.json', 'r') as f:
    intents = json.load(f)


patterns = []
tags = []
for intent in intents['intents']:
    for pattern in intent['patterns']:
        patterns.append(pattern)
        tags.append(intent['tag'])

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(patterns)

def get_response(user_input):
    """
    Finds the most relevant response for a user's query.
    """
    
    user_input_vec = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_input_vec, X)
    most_similar_idx = np.argmax(similarities)
    if similarities[0, most_similar_idx] > 0.3:  
        tag = tags[most_similar_idx]
        for intent in intents['intents']:
            if intent['tag'] == tag:
                return random.choice(intent['responses'])
    
    return "I'm sorry, I don't understand that. Can you please rephrase?"


@app.route("/")
def index():
    return render_template("index.html")
@app.route("/get_response", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    
    response = get_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)