import streamlit as st
import google.generativeai as genai
from textblob import TextBlob
import os
from datetime import datetime
import time
from dotenv import load_dotenv
from exercise import RelaxationExercises, get_relaxation_tips
from prompt import PromptBuilder, QUICK_RESPONSES, get_motivational_quote
from sentiment import SentimentAnalyzer

# #streamlit lite api
# # Safe way to access your Gemini API key from Streamlit secrets
# import requests
# import json
# API_KEY = st.secrets["GEMINI_API_KEY"]

# # Set up headers for API call
# headers = {
#     "Authorization": f"Bearer {API_KEY}",
#     "Content-Type": "application/json"
# }

# # Example request to Gemini endpoint
# url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

# data = {
#     "contents": [{"parts": [{"text": "Hello Gemini!"}]}]
# }

# response = requests.post(url, headers=headers, json=data)

# st.write(response.json())

# ✅ Initialize helper classes
sentiment_analyzer = SentimentAnalyzer()
prompt_builder = PromptBuilder()
relaxation_exercises = RelaxationExercises()

load_dotenv()
st.set_page_config(
    page_title="Mental Health Companion",
    page_icon="🧘",
    layout="centered"
)


st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
    }
    .user-message {
        background-color: #e3f2fd;
        align-items: flex-end;
    }
    .bot-message {
        background-color: #f3e5f5;
        align-items: flex-start;
    }
    </style>
""", unsafe_allow_html=True)


if "gemini_configured" not in st.session_state:
    
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        st.error("⚠️ GEMINI_API_KEY not found! Please set it in your environment or .env file")
        st.stop()
    
    genai.configure(api_key=api_key)
    st.session_state.gemini_configured = True
    st.session_state.model = genai.GenerativeModel('gemini-2.5-flash')


if "messages" not in st.session_state:
    st.session_state.messages = []


if "mood_history" not in st.session_state:
    st.session_state.mood_history = []


def analyze_sentiment(text):
    """Sentiment analysis using TextBlob"""
    text_lower = text.lower()
    
   
    mood_keywords = {
        'stressed': ['stress', 'stressed', 'pressure', 'overwhelmed', 'exam', 'anxious', 'anxiety', 'deadline'],
        'sad': ['sad', 'depressed', 'lonely', 'unhappy', 'cry', 'crying', 'hurt', 'pain', 'down'],
        'happy': ['happy', 'good', 'great', 'excited', 'wonderful', 'amazing', 'joy', 'love', 'grateful'],
        'angry': ['angry', 'mad', 'furious', 'frustrated', 'annoyed', 'hate']
    }
    
    mood_emojis = {
        'stressed': '😰',
        'sad': '😢',
        'happy': '😊',
        'angry': '😠',
        'neutral': '😐'
    }
    
   
    for mood, keywords in mood_keywords.items():
        if any(keyword in text_lower for keyword in keywords):
            return mood, mood_emojis[mood]
    
    
    try:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        
        if polarity < -0.3:
            return "sad", mood_emojis['sad']
        elif polarity < 0:
            return "stressed", mood_emojis['stressed']
        elif polarity > 0.3:
            return "happy", mood_emojis['happy']
        else:
            return "neutral", mood_emojis['neutral']
    except:
        return "neutral", mood_emojis['neutral']

def is_crisis(text):
    """Detect if message indicates crisis"""
    crisis_keywords = ['suicide', 'kill myself', 'end it all', 'self harm', 'hurt myself', 'want to die']
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in crisis_keywords)

def get_relaxation_tip(mood):
    """Get mood-specific tips"""
    tips = {
        "stressed": [
            "🌬️ Try the 4-7-8 breathing: Breathe in for 4s, hold for 7s, exhale for 8s",
            "🚶 Take a 5-minute walk outside",
            "📝 Write down 3 things you're grateful for",
            "💧 Drink a glass of water slowly - hydration helps"
        ],
        "sad": [
            "🎵 Listen to your favorite uplifting music",
            "📞 Call a friend or family member",
            "🌅 Get some sunlight - even 10 minutes helps",
            "📖 Read something comforting"
        ],
        "anxious": [
            "🧘 Practice grounding: Name 5 things you see, 4 you hear, 3 you touch",
            "💪 Do some light stretching or yoga",
            "📖 Read something comforting",
            "🌬️ Focus on slow, deep breaths"
        ],
        "angry": [
            "🥊 Do physical exercise - channel that energy productively",
            "🌬️ Try box breathing: In-4, Hold-4, Out-4, Hold-4",
            "🚶 Take a walk to cool down"
        ],
        "happy": [
            "📝 Write down what made you happy",
            "🎉 Share your joy with someone",
            "💪 Use this energy for something creative"
        ]
    }
    return tips.get(mood, ["💙 Remember, you're doing your best!"])

def generate_response(user_message, mood, chat_history=None):
    """Generate AI response with context"""
    
    if chat_history is None:
        chat_history = st.session_state.get("messages", [])

    
    if sentiment_analyzer.is_crisis(user_message):
        return prompt_builder.get_crisis_response()
    
   
    full_prompt = prompt_builder.build_prompt(user_message, mood, chat_history)
    
    try:
        response = st.session_state.model.generate_content(full_prompt)
        
        
        if hasattr(response, "text") and response.text:
            return response.text
        elif hasattr(response, "candidates") and response.candidates:
            return response.candidates[0].content.parts[0].text
        else:
            return "I'm here to listen. Could you tell me more about how you're feeling?"

    except Exception as e:
        st.error(f"⚠️ Error generating response: {e}")
        return "I'm here to listen. Could you tell me more about how you're feeling?"





with st.sidebar:
    st.title("🧘 Your Wellness Space")
    
    # Mood tracker
    st.subheader("📊 Mood Tracker")
    if st.session_state.mood_history:
        moods = [m[1] for m in st.session_state.mood_history[-7:]]
        st.write(" ".join(moods))
    else:
        st.write("Start chatting to track your mood!")
    
    st.divider()
    
    
    st.subheader("🌬️ Quick Calm")
    if st.button("Start Breathing Exercise"):
        progress_text = st.empty()
        progress_bar = st.progress(0)
        
       
        progress_text.info("🌬️ Breathe in...")
        for i in range(4):
            progress_bar.progress((i + 1) * 25)
            time.sleep(1)
        
       
        progress_text.warning("⏸️ Hold...")
        for i in range(7):
            time.sleep(1)
        
        
        progress_text.success("💨 Breathe out...")
        for i in range(8):
            progress_bar.progress(100 - (i * 12))
            time.sleep(1)
        
        progress_text.success("✅ Great job! Feel calmer?")
        st.balloons()
    
    st.divider()
    
    
    st.subheader("🆘 Need Help?")
    st.write("**Crisis Helplines:**")
    st.write("🇮🇳 iCall: 9152987821")
    st.write("🇮🇳 Vandrevala: 1860-2662-345")
    st.write("🇮🇳 AASRA: 91-9820466726")
    
    st.divider()
    
   
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.session_state.mood_history = []
        st.rerun()


st.title("💙 Mental Health Companion")
st.caption("A safe space to share your thoughts")

#
with st.expander("⚠️ Important Notice"):
    st.warning("""
    This chatbot is for emotional support only and is NOT a replacement for professional mental health care.
    If you're in crisis, please contact a mental health professional or helpline immediately.
    """)


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
        if message["role"] == "assistant" and "mood" in message:
            st.caption(f"Detected mood: {message['mood']} {message['emoji']}")



if prompt := st.chat_input("Share what's on your mind..."):
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
   
    mood, emoji, polarity = sentiment_analyzer.analyze(prompt)
    
   
    response = generate_response(prompt, mood, st.session_state.messages)
    
   
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            st.write(response)
            st.caption(f"Detected mood: {mood} {emoji}")
            
            
            if not sentiment_analyzer.is_crisis(prompt):
                tips = get_relaxation_tips(mood)
                with st.expander("💡 Helpful Tip"):
                    st.info(tips[0])
    
    
    st.session_state.messages.append({
        "role": "assistant",
        "content": response,
        "mood": mood,
        "emoji": emoji
    })


    
    
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_response(prompt, mood)
            st.write(response)
            st.caption(f"Detected mood: {mood} {emoji}")
            
            
            if not sentiment_analyzer.is_crisis(prompt):
                tips = get_relaxation_tips(mood)
                with st.expander("💡 Helpful Tip"):
                    st.info(tips[0])

    
    
    st.session_state.messages.append({
        "role": "assistant",
        "content": response,
        "mood": mood,
        "emoji": emoji
    })


st.divider()
st.caption("Made with 💜 for student wellbeing")
