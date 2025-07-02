import random
class QuestionStore:
    """ A class to manage a collection of question types for a quiz game. """

    def __init__(self, difficulty):
        
        self.difficulty = difficulty
        
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

    def ask_social_question(self):
    """ A method to ask a social question based on difficulty level. """
        country = random.choice(list(self.social_question[self.difficulty].keys()))
        correct_answer = self.social_question[difficulty][country]
        user_input = input(f"What is the capital of {country}? ").strip().lower()
        if user_input == correct_answer.lower():
            print("✅ Correct!")

        else:
            print(f"❌ Incorrect. The correct answer is {correct_answer}.")