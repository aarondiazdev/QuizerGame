from tkinter import Tk, PhotoImage, Canvas, Label, Button
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
  def __init__(self, quiz_brain: QuizBrain):
    self.quiz = quiz_brain
    
    self.window = Tk()
    self.window.title("Quizzler By Aaron Diaz")
    self.window.config(padx=20, pady=20, bg=THEME_COLOR)
    self.window.resizable(False, False)
    
    self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
    self.score_label.grid(row=0, column=1)
    
    self.canvas = Canvas(width=300, height=250, bg="white")
    self.question_text = self.canvas.create_text(150, 125, width=280, text="some question test", fill=THEME_COLOR, font=("Arial", 20, "italic"))
    self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
    
    self.true_image = PhotoImage(file="images/true.png")
    self.true_button = Button(image=self.true_image, highlightthickness=0, command=lambda:self.check_question("True"))
    self.true_button.grid(row=2, column=0)
    
    self.false_image = PhotoImage(file="images/false.png")
    self.false_button = Button(image=self.false_image, highlightthickness=0, command=lambda:self.check_question("False"))
    self.false_button.grid(row=2,column=1)

    self.get_next_question()
    self.window.mainloop()
    

  def get_next_question(self):
    q_text = self.quiz.next_question()
    self.canvas.itemconfig(self.question_text, text=q_text)
    self.reset_color()

  def reset_color(self):
    self.canvas.config(bg="white")

  def change_color(self, status):
    if status == "True":
      self.canvas.config(bg="green")
    else:
      self.canvas.config(bg="red")
    self.window.after(1000,self.get_next_question)
    

  def check_qty_questions(self):
    if not self.quiz.still_has_questions():
      self.reset_color()
      self.canvas.itemconfig(self.question_text, fill="black", text=f"Your score is: {str(self.quiz.score)}/{str(self.quiz.question_number)}")
      self.true_button.config(state="disabled")
      self.false_button.config(state="disabled")
      return False
    return True
      
  def check_question(self, user_option):
    if self.check_qty_questions():
      if self.quiz.check_answer(user_option):
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.change_color("True") 
      else:
        self.change_color("False")

        
    




 
    