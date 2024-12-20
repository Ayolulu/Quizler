from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#FF69B4"

class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.window.attributes('-fullscreen', True)
        self.canvas = Canvas(width=1400,height=700,bg="white",highlightthickness=0)
        self.canvas.grid(column=0,row=1,columnspan = 2)
        self.canvas_text = self.canvas.create_text(700,300,width=650,text="Some text is written here",fill=THEME_COLOR,font=("Arial",44))
        self.score = Label(text="Score: 0", font=("Arial", 50, "italic"),bg=THEME_COLOR)
        self.score.grid(column=0, row=0)
        self.true_img = PhotoImage(file="images/true.png")
        self.true_but= Button(image=self.true_img,highlightthickness=0,highlightcolor=THEME_COLOR,command=self.check_if_true)
        self.true_but.grid(column=0,row=2)
        self.false_img = PhotoImage(file="images/false.png")
        self.false_but = Button(image=self.false_img,highlightthickness=0,highlightcolor=THEME_COLOR,command=self.check_if_False)
        self.false_but.grid(column=1,row=2)
        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text,text= q_text)
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.canvas_text,text="Done!")
            self.true_but.config(state="disabled")
            self.false_but.config(state="disabled")
    def check_if_true(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)
    def check_if_False(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)
    def give_feedback(self,is_right):
        if is_right is True:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)





