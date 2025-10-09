from typing import List, Dict
import random

class RelaxationExercises:
    """Collection of relaxation and coping techniques"""
    
    def __init__(self):
        self.breathing_exercises = [
            {
                'name': '4-7-8 Breathing',
                'description': 'A calming breath pattern',
                'steps': [
                    'Breathe in through nose for 4 seconds',
                    'Hold your breath for 7 seconds',
                    'Exhale slowly through mouth for 8 seconds',
                    'Repeat 3-4 times'
                ],
                'duration': '2-3 minutes',
                'best_for': 'stress and anxiety'
            },
            {
                'name': 'Box Breathing',
                'description': 'Used by Navy SEALs for calm focus',
                'steps': [
                    'Breathe in for 4 seconds',
                    'Hold for 4 seconds',
                    'Breathe out for 4 seconds',
                    'Hold for 4 seconds',
                    'Repeat 4-5 times'
                ],
                'duration': '2-4 minutes',
                'best_for': 'stress and focus'
            },
            {
                'name': 'Deep Belly Breathing',
                'description': 'Simple deep breathing',
                'steps': [
                    'Place one hand on your belly',
                    'Breathe in deeply through nose (belly rises)',
                    'Exhale slowly through mouth (belly falls)',
                    'Continue for 5-10 breaths'
                ],
                'duration': '2-5 minutes',
                'best_for': 'general relaxation'
            }
        ]
        
        self.grounding_techniques = [
            {
                'name': '5-4-3-2-1 Technique',
                'description': 'Ground yourself in the present moment',
                'steps': [
                    '5 things you can SEE around you',
                    '4 things you can TOUCH',
                    '3 things you can HEAR',
                    '2 things you can SMELL',
                    '1 thing you can TASTE'
                ]
            },
            {
                'name': 'Body Scan',
                'description': 'Progressive relaxation',
                'steps': [
                    'Sit or lie down comfortably',
                    'Notice sensations in your feet',
                    'Slowly move attention up through your body',
                    'Release tension as you notice it',
                    'Continue to the top of your head'
                ]
            }
        ]
    
    def get_exercise_by_mood(self, mood: str) -> Dict:
        """Get appropriate exercise based on mood"""
        if mood in ['stressed', 'anxious']:
            return self.breathing_exercises[0]  # 4-7-8 breathing
        elif mood == 'angry':
            return self.breathing_exercises[1]  # Box breathing
        else:
            return self.breathing_exercises[2]  # Deep breathing
    
    def get_random_exercise(self) -> Dict:
        """Get a random breathing exercise"""
        return random.choice(self.breathing_exercises)
    
    def get_grounding_technique(self) -> Dict:
        """Get a grounding technique"""
        return random.choice(self.grounding_techniques)


def get_relaxation_tips(mood: str) -> List[str]:
    """
    Get mood-specific relaxation tips
    
    Args:
        mood: Current detected mood
        
    Returns:
        List of helpful tips
    """
    tips = {
        'stressed': [
            "🌬️ Try the 4-7-8 breathing: Breathe in for 4s, hold for 7s, exhale for 8s",
            "🚶 Take a 5-minute walk outside or around your room",
            "📝 Write down what's stressing you - getting it out helps",
            "💧 Drink a glass of water slowly - hydration helps your brain",
            "🎵 Listen to calming music or nature sounds",
            "📱 Take a break from screens for 10 minutes",
            "🧘 Do 5 minutes of gentle stretching"
        ],
        'sad': [
            "🌅 Get some sunlight - even 10 minutes helps your mood",
            "📞 Call or message someone you trust",
            "🎵 Listen to your favorite uplifting music",
            "📖 Read something comforting or inspiring",
            "🖼️ Look at photos that make you smile",
            "🌱 Do one small thing you enjoy, even if you don't feel like it",
            "💙 Be kind to yourself - you're doing your best"
        ],
        'anxious': [
            "🧘 Practice grounding: Name 5 things you see, 4 you hear, 3 you touch",
            "💪 Do some light physical activity - jumping jacks, stretches",
            "📝 Write down your worries, then write 'I'll handle this'",
            "🌬️ Focus on slow, deep breaths - anxiety can't survive calm breathing",
            "☕ Limit caffeine - it can increase anxiety",
            "📱 Use a calming app or meditation for 5 minutes",
            "🎯 Focus on what you CAN control, let go of what you can't"
        ],
        'angry': [
            "🥊 Do physical exercise - channel that energy productively",
            "🌬️ Try box breathing: In-4, Hold-4, Out-4, Hold-4",
            "📝 Write an angry letter (don't send it!) to vent",
            "🚶 Take a walk to cool down",
            "💪 Tense and release your muscles - progressive relaxation",
            "🎯 Count backwards from 100 by 7s to distract your mind",
            "🗣️ Talk it out with someone you trust"
        ],
        'happy': [
            "📝 Write down what made you happy - it helps remember good moments",
            "🎉 Share your joy with someone - happiness grows when shared",
            "📸 Take a mental snapshot of this moment",
            "🌟 Acknowledge yourself - you deserve this happiness",
            "💪 Use this energy for something creative or productive",
            "🎵 Dance to your favorite song - celebrate!",
            "💙 Pay it forward - do something kind for someone else"
        ],
        'neutral': [
            "🧘 Check in with yourself - how are you really feeling?",
            "📝 Journal for 5 minutes about your day",
            "🌱 Set one small intention for today",
            "💧 Stay hydrated - drink some water",
            "🚶 Take a short walk to refresh your mind",
            "📖 Read something interesting or educational",
            "🎯 Do one thing that brings you joy"
        ]
    }
    
    return tips.get(mood, tips['neutral'])


def get_quick_coping_strategies() -> List[str]:
    """Get general quick coping strategies"""
    return [
        "🌬️ Take 3 deep breaths right now",
        "💧 Drink a glass of water",
        "🚶 Walk around for 2 minutes",
        "🧊 Hold an ice cube - it grounds you instantly",
        "🎵 Listen to one calming song",
        "📱 Put your phone on 'Do Not Disturb' for 15 minutes",
        "🖐️ Press your palms together firmly for 10 seconds",
        "👀 Look out a window and name 5 things you see",
        "🌱 Smell something pleasant (hand cream, coffee, etc.)",
        "💪 Stretch your arms and roll your shoulders"
    ]


def get_self_care_reminder() -> str:
    """Get a random self-care reminder"""
    reminders = [
        "💧 Have you had water today? Hydration helps your mood!",
        "🍽️ Have you eaten something nutritious today?",
        "😴 Are you getting enough sleep? Rest is important for mental health.",
        "🚶 Have you moved your body today? Even a short walk helps!",
        "📱 Have you taken a break from screens? Your eyes (and mind) need rest.",
        "🧘 Have you taken a moment to breathe deeply today?",
        "💙 Have you been kind to yourself today? You deserve it.",
        "📞 Have you connected with someone you care about today?"
    ]
    
    return random.choice(reminders)


def format_breathing_exercise(exercise: Dict) -> str:
    """
    Format breathing exercise for display
    
    Args:
        exercise: Dictionary containing exercise details
        
    Returns:
        Formatted string for display
    """
    output = f"🌬️ **{exercise['name']}**\n\n"
    output += f"_{exercise['description']}_\n\n"
    output += "**Steps:**\n"
    
    for i, step in enumerate(exercise['steps'], 1):
        output += f"{i}. {step}\n"
    
    output += f"\n⏱️ Duration: {exercise['duration']}\n"
    output += f"✨ Best for: {exercise['best_for']}"
    
    return output


# Crisis resources
CRISIS_RESOURCES = {
    'India': [
        {
            'name': 'iCall Helpline',
            'number': '9152987821',
            'availability': 'Monday-Saturday, 8am-10pm',
            'email': 'icall@tiss.edu'
        },
        {
            'name': 'Vandrevala Foundation',
            'number': '1860-2662-345',
            'availability': '24/7',
            'info': 'Free, confidential'
        },
        {
            'name': 'AASRA',
            'number': '91-9820466726',
            'availability': '24/7',
            'email': 'aasrahelpline@yahoo.com'
        }
    ]
}


def get_crisis_resources() -> str:
    """Get formatted crisis resources"""
    output = "🆘 **Crisis Helplines (India):**\n\n"
    
    for resource in CRISIS_RESOURCES['India']:
        output += f"**{resource['name']}**\n"
        output += f"📞 {resource['number']}\n"
        output += f"⏰ {resource['availability']}\n"
        if 'email' in resource:
            output += f"✉️ {resource['email']}\n"
        output += "\n"
    
    return output