# College-Information-Chatbot
College Information Chatbot- Built AI chatbot using Python (Flask) with intent-based NLP- Designed JSON-based intent classification system- Developed interactive UI and backend integration for real-time responses

# Flask NLP Chatbot 🤖

A lightweight, retrieval-based chatbot built with **Python**, **Flask**, and **Scikit-Learn**. This application uses natural language processing (NLP) to match user queries with predefined intents using TF-IDF vectorization and cosine similarity.

## 🚀 Features
* **TF-IDF Vectorization**: Converts text patterns into numerical vectors to understand context.
* **Cosine Similarity**: Measures the distance between user input and known patterns to find the best match.
* **Flask Web Server**: A simple API backend to handle real-time messaging.
* **JSON-Driven**: Easy to expand the chatbot's knowledge by simply editing the `intents.json` file.

## 🛠️ Tech Stack
* **Backend**: Python, Flask
* **Machine Learning**: Scikit-Learn (TfidfVectorizer, Cosine Similarity)
* **Data Handling**: NumPy, JSON

## 📋 Prerequisites
Ensure you have Python 3.x installed. You will also need to install the following dependencies:
```bash
pip install flask scikit-learn numpy
```

## 📂 Project Structure
* `app.py`: The core Flask application and NLP logic.
* `intents.json`: The database of patterns and responses.
* `templates/index.html`: The frontend user interface.

## ⚙️ How It Works
1.  **Data Loading**: The app reads `intents.json` and flattens the patterns and tags.
2.  **Vectorization**: It uses `TfidfVectorizer` to create a matrix of "important" words from your training patterns.
3.  **Inference**: When a user sends a message, the app transforms that message into a vector and compares it against the matrix using **Cosine Similarity**.
4.  **Thresholding**: If the similarity score is above **0.3**, it returns a random response from the matching intent; otherwise, it asks for clarification.

## 🏃 Launching the App
1. Clone this repository.
2. Ensure `intents.json` is in the root directory.
3. Run the application:
   ```bash
   python app.py
   ```
4. Open your browser and navigate to `http://127.0.0.1:5000`.

## 📝 Customization
To add more "brains" to your bot, update the `intents.json` file:
```json
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": ["Hi", "Hello", "Hey"],
      "responses": ["Hello! How can I help you today?", "Hey there!"]
    }
  ]
}
```
