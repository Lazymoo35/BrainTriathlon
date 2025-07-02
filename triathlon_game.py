from question_store import QuestionStore
from ui import UI

class TriathlonGame:
    def __init__(self):
        self.question_store = QuestionStore()
        self.score = 0
        self.total_questions = 3
    
    def play(self):
        """Main Game Section"""
        UI.display_welcome()
        difficulty = UI.difficulty()

        self.play_round("Social Question", self.question_store.get_social_question, difficulty)
        self.play_round("Math Question", self.question_store.get_math_question, difficulty)
        self.play_round("Word Question", self.question_store.get_word_question, difficulty)

        UI.display_final_score(self.score, self.total_questions)

    def play_round(self, title, get_question_return, difficulty):
        """ Round-by-round repetition """
        UI.clear_screen()
        print(f"\n=== {title} Round ===\n")
        prompt, correct_answer = get_question_return(difficulty)
        answer = UI.ask_question(prompt)
        correct_check = answer.strip().lower() == correct_answer.lower()
        if correct_check:
            self.score += 1
        
        UI.display_feedback(correct_check, correct_answer)
        input("\nPress Enter to continue to the next round...")