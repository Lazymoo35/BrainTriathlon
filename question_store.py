import random
import operator

class QuestionStore:
    """ A class to manage a collection of questions for a quiz game. """

    def __init__(self):
        self.social_question = {
            "easy": {
                "France": "Paris",
                "Italy": "Rome",
                "United Kingdom": "London",
                "Indonesia": "Jakarta",
                "Thailand": "Bangkok",
                "Singapore": "Singapore",
                "Japan": "Tokyo",
                "China": "Beijing",
                "South Korea": "Seoul",
                "Australia": "Canberra"               
            },

            "medium": {
                "Poland": "Warsaw",
                "Czech Republic": "Prague",
                "Greece": "Athens",
                "Philippines": "Manila",
                "Timor Leste": "Dili",
                "Vietnam": "Hanoi",
                "Turkey": "Ankara",
                "Egypt": "Cairo",
                "Saudi Arabia": "Riyadh",
                "Canada": "Ottawa"
            },

            "hard": {
                "Ireland": "Dublin",
                "Sweden": "Stockholm",
                "Portugal": "Lisbon",
                "North Korea": "Pyongyang",
                "Pakistan": "Islamabad",
                "Morrocco": "Rabat",
                "Cuba": "Havana",
                "Peru": "Lima",
                "South Africa": "Pretoria",
                "New Zealand": "Wellington"
            }
        }

        self.operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.floordiv
        }

        self.word_question = {
            "easy": [
                "apple", "house", "water", "music", "happy", "green", "table", "chair", "light", "clock", "money", "coffee", "pizza", "school", "phone", "train", "river", "bread", "candy", "cloud", "paper", "window", "flower", "guitar", "doctor", "family", "yellow", "animal", "mountain", "orange", "pencil", "friend", "cookie", "banana", "beach", "sleep", "market", "camera", "jacket", "shoes", "island", "bottle", "mirror", "garden", "cheese", "letter", "engine", "planet", "rocket", "castle"
            ],

            "medium": [
                "hospital", "library", "language", "holiday", "traffic", "problem", "animal", "message", "weather", "village", "airport", "journey", "plastic", "history", "science", "company", "picture", "battery", "visitor", "machine", "address", "project", "student", "kitchen", "festival", "teacher", "painter", "country", "message", "program", "manager", "opinion", "natural", "subject", "engineer", "balance", "laundry", "passenger", "forever", "include", "shelter", "feather", "carrier", "station", "pattern", "travel", "meeting", "factory", "recycle", "content"
            ],

            "hard": [
                "approval", "strategy", "solution", "decision", "economy", "argument", "attitude", "benefit", "consumer", "creativity", "culture", "election", "evidence", "exercise", "freedom", "function", "generation", "industry", "influence", "location", "material", "movement", "opposite", "position", "positive", "pressure", "reaction", "reduction", "relation", "research", "resource", "response", "security", "selection", "situation", "society", "standard", "strength", "struggle", "suggestion", "symbol", "technique", "temperature", "tradition", "transport", "universe", "violence", "warning", "weakness", "witness"
            ]
        }

    def get_social_question(self, difficulty):
    """ A method to ask a social question based on difficulty level. """
        country = random.choice(list(self.social_question[self.difficulty].keys()))
        correct_answer = self.social_question[difficulty][country]
        social_prompt = f"What is the capital of {country}? "
        return (prompt, correct_answer)
    
    def get_math_question(self, difficulty):
    """ A method to formulate math question based on difficulty level. """
        if difficulty == "easy"
            num1 = random.randint(1, 20)
            num2 = random.randint(1, 10)
        elif difficulty == "medium":
            num1 = random.randint(5, 50)
            num2 = random.randint(5, 20)
        else difficulty == "hard":
            num1 = random.randint(15, 30)
            num2 = random.randint(15, 20)
        
        op_symbol = random.choice(list(self.operations.keys()))
        op_func = self.operations[op_symbol]

        correct_answer = op_func(num1, num2)
        math_prompt = f"What is {num1} {op_symbol} {num2}?"

        return (math_prompt, str(correct_answer))
    
    def get_word_question(self, difficulty):
    """ A method to ask word question based on difficulty level. """
        word = random.choice(self.word_question[difficulty]).upper()
        puzzle = "".join("_" if c in "AEIOU" else c for c in word)
        
i       word_prompt = f"Guess the word: {puzzle}"
        return (word_prompt, word)