import html
from tkinter import *
from constants import category_options, difficulty_options, question_type_options
from label_component import CustomLabel
from question_ui import QuestionUi
from side_bar import CustomMenuSide
import random

# constant
BG_SIDE_BAR_FRAME = "#CAE0BC"
BG_SCREEN = "#EAFAEA"

# title label style
quiz_title_label = {
    "padding": (5, 5),
    "font": ("Arial", 20, "bold"),
    "bg_color": BG_SCREEN,
    "fg_color": "#780C28",
    "anchor": "center"

}

questions = []


def handle_questions(questions_list):
    global questions
    questions = questions_list
    question_ui = QuestionUi(main_frame, questions)


# Create the root window
root = Tk()
root.geometry("400x200")  # Initial window size
root.title("Quiz App")
root.configure(bg=BG_SCREEN)

main_frame = Frame(root)
main_frame.config(bg=BG_SCREEN)
main_frame.pack(fill="both", side="right", expand=True)
title_label = CustomLabel(main_frame, text="Discover your knowledge",
                          padding=quiz_title_label["padding"], font=quiz_title_label["font"],
                          bg=quiz_title_label["bg_color"], fg=quiz_title_label["fg_color"],
                          anchor=quiz_title_label["anchor"])

menu_side = CustomMenuSide(root, on_retrieve_questions=handle_questions)

root.mainloop()
