import os

class UI:
    "A class to handle user interface thingies :)"

    def clear_screen(self):
        """Clears the terminal."""
        os.system('cls')

    def display_welcome(self):
        """Displays the welcome message for the game."""
        self.clear_screen()
        print("  WELCOME TO THE TRIATHLON QUIZ!   ")
        print("===================================")
        print("\nYou will run through 3 brain excercises.")
        print("Do you best!\n")
        input("Press Enter to start...")

    def difficulty(self):
        """Asks the user for a difficulty level."""
        while True:
            level = input("Choose a difficulty (easy, medium, hard): ").lower().strip()
            if level in ["easy", "medium", "hard"]:
                return level
            else:
                print("Invalid choice. Please type 'easy', 'medium', or 'hard'.")

    def ask_question(self, prompt):
        """Displays a question prompt and returns the user's stripped answer."""
        print("\n" + "-"*30)
        return input(f"{prompt}\n: ").strip()

    def display_feedback(self, correct_check, correct_answer):
        """Displays feedback to the user after they answer."""
        if correct_check:
            print("✅ Correct!")
        else:
            print(f"❌ Incorrect. The correct answer was: {correct_answer}")

    def display_final_score(self, score, total_questions):
        """Displays the final score at the end of the game."""
        print("\n===================================")
        print("           GAME OVER             ")
        print("===================================")
        print(f"\nYour final score is: {score} / {total_questions}")
        if score == total_questions:
            print("Perfect score! Congratulations! 🎉")
        elif score >= total_questions / 2:
            print("👍 Good job!")
        else:
            print("Better luck next time! :))")