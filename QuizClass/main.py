from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    temp = Question(question['text'],question['answer'])
    question_bank.append(temp)

my_quiz = QuizBrain(question_bank)
while my_quiz.still_has_questions():
    my_quiz.next_question()
print("You've complete the quiz.")
print(f"Your final score was: {my_quiz.score}/{my_quiz.question_number}")
