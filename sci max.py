import tkinter as tk
from tkinter import messagebox

class ScienceGame:
    def __init__(self, master):
        self.master = master
        self.score = 0
        self.current_question = 0
        
        self.questions = [
            {"question": "What is the smallest unit of life?", "answers": ["cell", "atom", "molecule"], "correct": "cell"},
            {"question": "What is the process by which plants make their own food?", "answers": ["photosynthesis", "respiration", "fermentation"], "correct": "photosynthesis"},
            {"question": "Which planet is known as the 'Red Planet'?", "answers": ["Mars", "Jupiter", "Venus"], "correct": "Mars"}
        ]
        
        self.question_label = tk.Label(master, text="", font=("Helvetica", 16))
        self.question_label.pack(pady=20)
        
        self.answer_buttons = []
        for i in range(3):
            button = tk.Button(master, text="", font=("Helvetica", 14), command=lambda x=i: self.check_answer(x), width=20, height=2, bg="white", bd=3)
            button.pack(pady=10)
            self.answer_buttons.append(button)
        
        self.score_label = tk.Label(master, text="Score: 0", font=("Helvetica", 14))
        self.score_label.pack(pady=20)
        
        self.next_question()
    
    def next_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.question_label.config(text=question["question"])
            for i in range(3):
                self.answer_buttons[i].config(text=question["answers"][i])
            self.current_question += 1
        else:
            self.question_label.config(text="Game Over!")
    
    def check_answer(self, answer_index):
        question = self.questions[self.current_question - 1]
        if question["answers"][answer_index] == question["correct"]:
            self.score += 1
            result = "Correct!"
        else:
            result = "Incorrect!"
        self.score_label.config(text="Score: {}".format(self.score))
        self.master.after(1000, self.next_question)
        tk.messagebox.showinfo("Result", result)
        

root = tk.Tk()
root.title("Science Quiz Game")
root.geometry("800x600")
root.state("zoomed")
game = ScienceGame(root)
root.mainloop()
