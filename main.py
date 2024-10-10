from question_model import Question
from data import Data
from quiz_brain import QuizBrain
from ui import QuizInterface

data = Data()
data.get_data()
question_bank = []
question_data = data.question_data

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
ui = QuizInterface(quiz)

