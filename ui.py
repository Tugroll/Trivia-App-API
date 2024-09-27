THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizUI:

    def __init__(self, quiz: QuizBrain):
        self.quizz = quiz
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(bg=THEME_COLOR)
        self.score_label = Label(text="Score", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, padx=20, pady=20, columnspan=2)
        self.question_text = self.canvas.create_text(
                150,
                125,
                width= 280,
                text="Some Questions",
                fill=THEME_COLOR,
                font= ("Arial", 20, "italic")
                )

        true_image = PhotoImage(file="images/true.png")
        self.false_button = Button(image=true_image,highlightthickness=0, command=self.true_pressed)
        self.false_button.grid(row=2, column=1)
        false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=false_image, highlightthickness=0,command=self.false_pressed)
        self.true_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quizz.still_has_questions():

            the_question = self.quizz.next_question()
            self.score_label.config(text=f"Score: {self.quizz.score}")
            self.canvas.itemconfig(self.question_text, text=the_question)
        else:
            self.canvas.itemconfig(self.question_text,text="No More Question")

            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quizz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quizz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
