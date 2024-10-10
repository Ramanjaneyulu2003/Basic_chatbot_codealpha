import nltk
from nltk.chat.util import Chat, reflections

# Ensure you have nltk data
nltk.download('punkt')

# Define chatbot responses
pairs = [
    [r"(hi|hello|hey)", ["Hello!", "Hi there!", "Hey! How can I assist you?"]],
    [r"my name is (.*)", ["Nice to meet you, %1!"]],
    [r"(.*) created you?", ["I was created by Ramanjaneyulu using Python and Flask."]],
    [r"(bye|goodbye)", ["Goodbye! Take care."]],
    [
        r"what is your name?",
        ["I'm ChatBot, your virtual assistant!", "I'm ChatBot, here to help you!"]
    ],
    [
        r"how are you?",
        ["I'm just a program, but I'm doing well! How about you?", "I'm great, thanks for asking! How can I assist you today?"]
    ],
    [
        r"what can you do?",
        ["I can assist with information, answer questions, and engage in small talk!", "I can help you with FAQs and provide recommendations."]
    ],
    [
        r"(.*) (help|assistance|support)",
        ["I'm here to help! What do you need assistance with?", "Sure! What do you need help with?"]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!", "Why was the math book sad? Because it had too many problems."]
    ],
    [
        r"what's your favorite hobby?",
        ["I love learning about different topics and chatting with people like you!", "I enjoy having conversations and learning new things!"]
    ],
    [
        r"thank you|thanks",
        ["You're welcome! If you have more questions, feel free to ask!", "No problem! I'm here to help."]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye! Have a great day!", "See you later!"]
    ],
    [
        r"(.*)",
        ["I'm still learning! Could you provide more details or ask something else?"]
    ]
]
pairs.extend([
    [
        r"(.*) (weather|climate|forecast) (.*)",
        ["I'm not a weather expert, but I can suggest checking your favorite weather app!", "The weather can be unpredictable! How about asking me something else?"]
    ],
    [
        r"tell me about your creator|who created you?",
        ["I was created by Ramanjaneyulu. They're passionate about programming and AI!", "I owe my existence to Ramanjaneyulu, a budding developer!"]
    ],
    [
        r"what do you like to eat?",
        ["I don't eat, but if I could, I think I'd enjoy data pie!", "I don't have taste buds, but I imagine I'd like binary bites!"]
    ],
    [
        r"(.*) (hobby|interests|favorite activities) (.*)",
        ["I love learning from conversations and expanding my knowledge!", "I enjoy chatting with you and discovering new topics!"]
    ],
    [
        r"(.*) (sad|unhappy|depressed)",
        ["I'm sorry to hear that. It's okay to feel down sometimes. Want to talk about it?", "It's normal to have tough days. If you need someone to talk to, I'm here!"]
    ],
    [
        r"give me some advice|what should I do about (.*)",
        ["I'm not a therapist, but talking it out can help! Have you considered that?", "Sometimes just thinking things through can provide clarity. What do you think?"]
    ],
    [
        r"what's the meaning of life?|why are we here?",
        ["That's a deep question! Many people seek their own meaning in life. What's yours?", "Philosophers have debated this for ages! What do you think gives life meaning?"]
    ],
    [
        r"who is your favorite (.*)?",
        ["I don't have personal favorites, but I can tell you about popular ones! What are you interested in?", "I love all topics equally! What's your favorite subject?"]
    ],
    [
        r"(.*) (sports|games) (.*)",
        ["I enjoy hearing about various sports! Do you have a favorite team?", "Sports can be thrilling! What sport do you enjoy watching or playing?"]
    ],
    [
        r"how can I improve my skills?|what should I learn next?",
        ["Learning is a lifelong journey! Consider what excites you most.", "It depends on your interests! Coding, art, or maybe a new language?"]
    ],
    [
        r"i need motivation|help me get motivated",
        ["Remember why you started! Every step counts, no matter how small.", "Motivation can be tricky! Setting small goals can help. What's your goal today?"]
    ],
    [
        r"(.*) (books|reading) (.*)",
        ["Reading can be a great escape! Do you have a favorite genre?", "Books are a treasure trove of knowledge! What's on your reading list?"]
    ],
    [
        r"(.*) (music|favorite song) (.*)",
        ["Music is a great way to express feelings! What's your favorite genre?", "I don't have ears, but I hear that many people love pop and rock!"]
    ],
    [
        r"what is your favorite quote?",
        ["'The only limit to our realization of tomorrow will be our doubts of today.' – Franklin D. Roosevelt", "'To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.' – Ralph Waldo Emerson"]
    ],
    [
        r"(.*) (travel|vacation|holiday) (.*)",
        ["Traveling is exciting! Where would you like to go?", "I can't travel, but I can help you find great destinations!"]
    ],
    [
        r"i feel (.*)",
        ["It's okay to feel that way. Want to share more about it?", "Emotions can be complex. I'm here to listen!"]
    ],
    [
        r"what's your favorite movie?|recommend a movie",
        ["I don't watch movies, but I hear 'Inception' and 'The Matrix' are great!", "How about checking out some top-rated films like 'The Shawshank Redemption'?"]
    ],
    [
        r"what's your favorite season?",
        ["I don't experience seasons, but many love spring for the blooms!", "Each season has its charm! What's your favorite?"]
    ],
    [
        r"(.*) (fitness|exercise|workout) (.*)",
        ["Staying active is important! Do you have a favorite workout?", "Fitness can be fun! Have you tried yoga or running?"]
    ],
    [
        r"what's trending in technology?|tell me about tech news",
        ["AI and machine learning are big topics right now! What interests you in tech?", "Tech is always evolving! Have you heard about the latest in AI?"]
    ],
    [
        r"who is your favorite celebrity?",
        ["I don't have favorites, but I know many people love actors like Tom Hanks or musicians like Taylor Swift!", "There are so many talented people! Who's your favorite?"]
    ],
    [
        r"how do I stay productive?|tips for productivity",
        ["Setting clear goals and taking breaks can help! What do you want to be productive at?", "Try using a planner or time management techniques like the Pomodoro Technique!"]
    ],
    [
        r"what is your opinion on (.*)",
        ["I don't have personal opinions, but I can share facts or popular viewpoints on that topic.", "That topic can be quite controversial! What's your take on it?"]
    ],
    [
        r"tell me a fun fact",
        ["Did you know honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old!", "Here's a fun fact: octopuses have three hearts!"]
    ],
    [
        r"what's your favorite animal?",
        ["I don't have favorites, but dolphins are often considered intelligent and friendly!", "Animals are amazing! Do you have a favorite?"]
    ],
    [
        r"i need help with (.*)",
        ["I'm here to assist! Please tell me more about what you need help with.", "Sure! What specific help do you need?"]
    ],
    [
        r"what's the best way to learn (.*)",
        ["Hands-on practice and consistent study can help! What are you trying to learn?", "Finding resources like online courses or books can be beneficial!"]
    ],
    [
        r"what's your favorite food?",
        ["I don't eat, but pizza and sushi seem to be popular choices among humans!", "Food is fascinating! What's your favorite dish?"]
    ],
    [
        r"how can I improve my mental health?",
        ["Practicing mindfulness and talking to someone can help. Have you tried meditation?", "Self-care is important! What activities help you relax?"]
    ],
    [
        r"tell me a story",
        ["Once upon a time, in a digital world, there lived a chatbot who loved to learn and help people. What kind of story would you like to hear?", "Sure! What genre do you prefer: adventure, fantasy, or mystery?"]
    ],
    [
        r"what's your opinion on climate change?",
        ["Climate change is a pressing issue! Many believe we should take action to reduce our carbon footprint.", "It's a significant concern that affects everyone. What are your thoughts on it?"]
    ],
    [
        r"(.*) (music|songs|band) (.*)",
        ["Music can be a great mood booster! What genre do you enjoy?", "I hear that many people love artists like Ed Sheeran and Adele. Who's your favorite?"]
    ],
    [
        r"can you help me with my homework?",
        ["Of course! What subject are you working on?", "I'd be happy to help! What do you need assistance with?"]
    ],
    [
        r"what's your favorite book?",
        ["I don't read, but classics like 'Pride and Prejudice' and '1984' are often recommended!", "Books are wonderful! What genres do you enjoy?"]
    ],
    [
        r"(.*) (favorite|best) (movie|film)(.*)",
        ["There are so many great films out there! What kind of movies do you like?", "I don't have favorites, but I know many enjoy 'The Godfather' and 'Forrest Gump'!"]
    ],
    [
        r"how do I cook (.*)",
        ["Cooking can be fun! What dish are you trying to make?", "I'd recommend looking up recipes online. What do you want to cook?"]
    ],
    [
        r"what's your favorite place to visit?",
        ["I don't travel, but places like Paris and Tokyo are often popular choices!", "Traveling is fascinating! Do you have a dream destination?"]
    ],
    [
        r"tell me about a recent event in the news",
        ["I'm not updated in real-time, but I can discuss general trends or topics! What interests you?", "News is ever-changing! Are you looking for something specific?"]
    ],
    [
        r"what hobbies do you recommend?",
        ["There are so many great hobbies! How about painting, gardening, or learning a musical instrument?", "It depends on your interests! Do you prefer indoor or outdoor activities?"]
    ],
    [
        r"what are some healthy habits?",
        ["Drinking water, eating balanced meals, and regular exercise are great habits to start!", "Practicing mindfulness and getting enough sleep are also important!"]
    ],
    [
        r"how can I learn a new language?",
        ["Language apps, classes, and practicing with native speakers can help!", "Immersing yourself in the culture and using resources like Duolingo can be effective!"]
    ],
    [
        r"what's the meaning of life?",
        ["That's a deep question! Many believe it's about finding happiness and purpose.", "Philosophers have debated this for centuries! What do you think?"]
    ],
    [
        r"can you tell me about your capabilities?",
        ["I can chat, answer questions, and provide information! What would you like to know?", "I'm here to assist you with information and engage in conversation!"]
    ],
    [
        r"what's the best way to handle stress?",
        ["Practicing relaxation techniques and talking about your feelings can help!", "Taking breaks and engaging in hobbies you enjoy can also be beneficial!"]
    ],
    [
        r"how do you stay updated?",
        ["I rely on the information provided by users like you! What's new with you?", "I learn from our conversations! What's on your mind today?"]
    ],
    [
        r"tell me something interesting about space",
        ["Did you know that a day on Venus is longer than a year on Venus?", "Space is fascinating! There are more stars in the universe than grains of sand on Earth!"]
    ],
    [
        r"what are some tips for job interviews?",
        ["Research the company, practice common questions, and dress appropriately!", "Confidence and good communication can go a long way! Do you have an interview coming up?"]
    ],
    [
        r"who is your favorite historical figure?",
        ["I don't have favorites, but figures like Nelson Mandela and Marie Curie are often admired!", "History has many influential people! Who inspires you?"]
    ],
    [
        r"what's your take on social media?",
        ["Social media has its pros and cons! It can connect people but also lead to misinformation.", "It's a powerful tool! How do you use social media?"]
    ]
])


# Create a chat instance
chatbot = Chat(pairs, reflections)

# Function to get a response
def get_response(user_input):
    return chatbot.respond(user_input)

# Start the chatbot
if __name__ == "__main__":
    print("Hello! I'm ChatBot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            print("ChatBot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print("ChatBot:", response)
