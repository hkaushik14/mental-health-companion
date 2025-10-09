# Mental Health Companion Chatbot

## Project Overview

The Mental Health Companion Chatbot is a supportive AI-powered application designed to help students manage stress, anxiety, and other emotions through empathetic conversation and actionable tips. The chatbot provides a safe and friendly space for students to share their feelings, receive motivational quotes, and learn simple relaxation exercises.

## Features

* **Mood Detection:** Automatically detects the user's mood (stressed, sad, happy, anxious, angry, neutral) using keyword-based analysis and TextBlob sentiment analysis.
* **Context-Aware Responses:** Generates empathetic responses based on the user's mood and conversation history using the `PromptBuilder`.
* **Crisis Support:** Provides immediate professional helpline information if a crisis situation is detected.
* **Relaxation Tips:** Suggests practical relaxation exercises and mindfulness techniques to reduce stress.
* **Motivational Quotes:** Offers uplifting messages to encourage positive thinking.
* **Secure API Integration:** Uses `.env` for storing API keys securely, never exposed in the repository.

## Technologies Used

* **Python** for backend logic
* **Streamlit** for the web interface
* **Google Gemini API** for AI-generated responses
* **TextBlob** for sentiment analysis
* **dotenv** for environment variable management

## Sreenshot



## Project Structure

```
mental-health-companion/
│
├── app.py                # Main Streamlit app
├── exercise.py           # Relaxation exercises and tips
├── prompt.py             # Prompt builder for AI responses
├── sentiment.py          # Sentiment analysis logic
├── requirements.txt      # Python dependencies
├── .gitignore            # Ignore sensitive files like .env
├── README.md             # Project documentation
└── .env                  # API keys (not tracked in GitHub)
```

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/hkaushik14/mental-health-companion.git
cd mental-health-companion
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your API key:

```
GEMINI_API_KEY=your_api_key_here
```

4. Run the application:

```bash
streamlit run app.py
```

## Security Notice

* Never commit your `.env` file or API keys to GitHub.
* If any key is exposed, regenerate it immediately.

## Usage

* Enter your thoughts in the chat input.
* Receive mood detection and empathetic responses.
* Explore relaxation tips and motivational quotes.
* Use it as a supportive companion for mental wellbeing.

## License

This project is open-source and available under the MIT License.

