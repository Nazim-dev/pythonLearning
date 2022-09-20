class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.questions = question_list
        self.score = 0
        self.total = 0
    def still_has_questions(self):
        return self.question_number < len(self.questions)
        
    def next_question(self):
        ques = self.questions[self.question_number]
        self.question_number += 1
        response = input(f"Q.{self.question_number}: {ques.text} (True/False)? ")
        self.check_answer(response, ques.answer)


    def check_answer(self, response, answer):
        self.total += 1
        if response.lower() == answer.lower():
            print("Correct")
            self.score += 1
            print(f"Your current score is {self.score}/{self.total} ")
        else:
            print("Wrong")
            print(f"Your current score is {self.score}/{self.total} ")
        print("\n")

    def end(self):
        print("You've completed the quiz")
        print(f"Your final score is  {self.score}/{self.total}")