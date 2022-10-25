class QuizBrain:

    def __init__(self, ques_list):
        self.question_number = 0
        self.question_list = ques_list
        self.score = 0

    def next_question(self):
        q_num = self.question_number
        ques = self.question_list[q_num]
        self.question_number += 1
        answer = input(f"{self.question_number}: {ques.text} (True/False): ")
        self.check_answer(answer, ques.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
            print(f"Your current score is {self.score}/{self.question_number}")
            print()
        else:
            print("That's wrong!")
            print()