from textblob import TextBlob
from typing import Tuple

class SentimentAnalyzer:
    """Analyzes text sentiment and categorizes mood"""
    
    def __init__(self):
        self.mood_keywords = {
            'stressed': [
                'stress', 'stressed', 'pressure', 'overwhelmed', 'exam', 
                'anxious', 'anxiety', 'tension', 'worried', 'nervous',
                'deadline', 'burden', 'exhausted', 'tired'
            ],
            'sad': [
                'sad', 'depressed', 'lonely', 'unhappy', 'cry', 'crying',
                'hurt', 'pain', 'miserable', 'down', 'low', 'hopeless',
                'worthless', 'empty'
            ],
            'anxious': [
                'anxious', 'anxiety', 'panic', 'fear', 'scared', 'afraid',
                'worry', 'worried', 'nervous', 'uneasy', 'restless'
            ],
            'happy': [
                'happy', 'good', 'great', 'excited', 'wonderful', 'amazing',
                'fantastic', 'excellent', 'joy', 'cheerful', 'blessed',
                'grateful', 'thankful', 'love'
            ],
            'angry': [
                'angry', 'mad', 'furious', 'frustrated', 'annoyed', 'irritated',
                'hate', 'rage'
            ]
        }
        
        self.mood_emojis = {
            'stressed': '😰',
            'sad': '😢',
            'anxious': '😟',
            'happy': '😊',
            'angry': '😠',
            'neutral': '😐'
        }
    
    def analyze(self, text: str) -> Tuple[str, str, float]:
        """
        Analyze text and return mood, emoji, and sentiment score
        
        Args:
            text: User message text
            
        Returns:
            Tuple of (mood, emoji, polarity_score)
        """
        text_lower = text.lower()
        
        # Keyword-based detection (priority)
        for mood, keywords in self.mood_keywords.items():
            if any(keyword in text_lower for keyword in keywords):
                return mood, self.mood_emojis[mood], self._get_polarity(text)
        
        # TextBlob sentiment analysis (fallback)
        polarity = self._get_polarity(text)
        
        if polarity < -0.5:
            return 'sad', self.mood_emojis['sad'], polarity
        elif polarity < -0.1:
            return 'stressed', self.mood_emojis['stressed'], polarity
        elif polarity > 0.5:
            return 'happy', self.mood_emojis['happy'], polarity
        elif polarity > 0.1:
            return 'happy', self.mood_emojis['happy'], polarity
        else:
            return 'neutral', self.mood_emojis['neutral'], polarity
    
    def _get_polarity(self, text: str) -> float:
        """Get sentiment polarity score using TextBlob"""
        try:
            blob = TextBlob(text)
            return blob.sentiment.polarity
        except:
            return 0.0
    
    def get_intensity(self, polarity: float) -> str:
        """Get intensity level of emotion"""
        abs_polarity = abs(polarity)
        
        if abs_polarity > 0.7:
            return "very"
        elif abs_polarity > 0.4:
            return "quite"
        elif abs_polarity > 0.1:
            return "somewhat"
        else:
            return "slightly"
    
    def is_crisis(self, text: str) -> bool:
        """Detect if message indicates crisis/emergency"""
        crisis_keywords = [
            'suicide', 'kill myself', 'end it all', 'don\'t want to live',
            'self harm', 'hurt myself', 'die', 'death wish'
        ]
        
        text_lower = text.lower()
        return any(keyword in text_lower for keyword in crisis_keywords)


# Helper function for direct use
def analyze_sentiment(text: str) -> Tuple[str, str]:
    """
    Quick sentiment analysis function
    Returns (mood, emoji)
    """
    analyzer = SentimentAnalyzer()
    mood, emoji, _ = analyzer.analyze(text)
    return mood, emoji