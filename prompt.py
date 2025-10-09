from typing import List, Dict

class PromptBuilder:
    """Builds context-aware prompts for AI responses"""
    
    def __init__(self):
        self.base_system_prompt = """You are a supportive mental health companion chatbot designed for students.
Your purpose is to provide emotional support, empathy, and encouragement.

Guidelines:
- Be warm, empathetic, and non-judgmental
- Keep responses concise (2-4 sentences)
- Use simple, friendly language
- Validate feelings before offering advice
- Never claim to be a therapist or provide medical advice
- If user seems in crisis, gently suggest professional help
- Be culturally sensitive and inclusive
- Focus on hope and coping strategies
"""
    
    def build_prompt(self, user_message: str, mood: str, 
                     chat_history: List[Dict] = None) -> str:
        """
        Build complete prompt with context
        
        Args:
            user_message: Current user message
            mood: Detected mood (stressed, sad, anxious, etc.)
            chat_history: Previous conversation context
            
        Returns:
            Complete prompt string for AI
        """
        mood_context = self._get_mood_context(mood)
        
        prompt_parts = [
            self.base_system_prompt,
            f"\nCurrent situation: The user seems to be feeling {mood}.",
            mood_context,
            self._get_conversation_history(chat_history),
            f"\nUser: {user_message}",
            "\nRespond with empathy and support. Bot:"
        ]
        
        return "\n".join(prompt_parts)
    
    def _get_mood_context(self, mood: str) -> str:
        """Get specific guidance based on detected mood"""
        mood_prompts = {
            'stressed': """
The user is experiencing stress. Your response should:
- Acknowledge their feelings of stress
- Normalize the experience (stress is common)
- Offer a calming perspective
- Suggest they're capable of handling this
""",
            'sad': """
The user is feeling sad or down. Your response should:
- Validate their sadness without trying to 'fix' it immediately
- Show compassion and understanding
- Remind them that feelings are temporary
- Offer gentle encouragement
""",
            'anxious': """
The user is feeling anxious or worried. Your response should:
- Acknowledge their anxiety with understanding
- Help ground them in the present moment
- Offer reassurance without dismissing concerns
- Suggest small, manageable steps
""",
            'angry': """
The user is feeling angry or frustrated. Your response should:
- Validate their frustration
- Help them feel heard
- Avoid being dismissive
- Encourage healthy expression of feelings
""",
            'happy': """
The user is feeling positive. Your response should:
- Share in their joy
- Encourage them to savor the moment
- Be enthusiastic but not overly so
- Build on their positive energy
""",
            'neutral': """
The user's mood is neutral. Your response should:
- Be supportive and open
- Encourage them to share more if they wish
- Be a good listener
- Maintain a warm, friendly tone
"""
        }
        
        return mood_prompts.get(mood, mood_prompts['neutral'])
    
    def _get_conversation_history(self, chat_history: List[Dict]) -> str:
        """Format conversation history for context"""
        if not chat_history or len(chat_history) == 0:
            return "\n[This is the start of the conversation]"
        
        # Get last 3 exchanges for context
        recent = chat_history[-6:] if len(chat_history) > 6 else chat_history
        
        history_text = "\nRecent conversation:"
        for msg in recent:
            role = "User" if msg["role"] == "user" else "Bot"
            history_text += f"\n{role}: {msg['content']}"
        
        return history_text
    
    def get_crisis_response(self) -> str:
        """Get response for crisis situations"""
        return """I'm really concerned about what you're sharing. Your feelings are valid, but I want to make sure you're safe.

Please reach out to a mental health professional or crisis helpline right away:

🇮🇳 iCall Helpline: 9152987821 (Mon-Sat, 8am-10pm)
🇮🇳 Vandrevala Foundation: 1860-2662-345 (24/7)

You don't have to face this alone. Professional help can make a real difference. 💙"""
    
    def get_greeting_prompt(self) -> str:
        """Get initial greeting message"""
        return """Hello! I'm here to listen and support you. 💙

This is a safe space where you can share what's on your mind. Whether you're feeling stressed, happy, worried, or anything in between - I'm here for you.

How are you feeling today?"""


# Pre-defined quick responses
QUICK_RESPONSES = {
    'greeting': [
        "Hello! How are you feeling today?",
        "Hi there! I'm here to listen. What's on your mind?",
        "Welcome! How can I support you today?"
    ],
    'thanks': [
        "You're welcome! I'm here whenever you need support. 💙",
        "I'm glad I could help! Remember, I'm here for you.",
        "Happy to help! Take care of yourself."
    ],
    'goodbye': [
        "Take care! Remember, I'm here whenever you need to talk. 💙",
        "Goodbye! Be kind to yourself.",
        "See you soon! Don't hesitate to come back if you need support."
    ]
}


def get_motivational_quote() -> str:
    """Get a random motivational quote"""
    quotes = [
        "You are stronger than you think. 💪",
        "Small steps forward are still progress. 🌱",
        "It's okay to not be okay. What matters is that you're trying. ✨",
        "You've survived 100% of your worst days. You're doing great. 🌟",
        "Be gentle with yourself. You're doing the best you can. 💙",
        "Your feelings are valid, and so are you. 🌈",
        "Healing is not linear, and that's perfectly okay. 🌸",
        "You don't have to be positive all the time. It's okay to feel what you feel. 🦋"
    ]
    
    import random
    return random.choice(quotes)