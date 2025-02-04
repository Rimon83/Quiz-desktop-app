from button_component import CustomButton
from data import get_data
from tkinter import *

from label_component import CustomLabel
from menu_drop import MenuDrop
from spinbox_component import CustomSpinbox
from constants import category_options, difficulty_options, question_type_options

# constant
BG_SIDE_BAR_FRAME = "#CAE0BC"
BG_SCREEN = "#EAFAEA"

# menu side label style
LABEL_PADDING = (5, 5)
LABEL_FONT = ("Arial", 24)
LABEL_BG_COLOR = "#CAE0BC"
LABEL_FG_COLOR = "#780C28"
LABEL_ANCHOR = "center"

# start button style
BUTTON_PADDING = (5, 5)
BUTTON_BG = "#780C28"
BUTTON_FG = "#CAE0BC"
BUTTON_HOVER_BG = "#CAE0BC"
BUTTON_HOVER_FG = "#780C28"


class CustomMenuSide:
    def __init__(self, parent, on_retrieve_questions):
        self.on_retrieve_questions = on_retrieve_questions
        self.frame = Frame(parent)
        self.frame.config(bg=BG_SIDE_BAR_FRAME)
        self.frame.pack(fill="y", side="left")

        # sidebar
        self.label = CustomLabel(self.frame, text="Test Setting", fg=LABEL_FG_COLOR, bg=LABEL_BG_COLOR,
                                 font=LABEL_FONT, padding=LABEL_PADDING, anchor=LABEL_ANCHOR)
        self.amount_drop = CustomSpinbox(self.frame, from_value=1, to_value=50)
        self.category_drop = MenuDrop(self.frame, values=category_options, initial_value=category_options[0],
                                      width=40)
        self.difficulty_drop = MenuDrop(self.frame, values=difficulty_options, initial_value=difficulty_options[0],
                                        width=40)
        self.type_drop = MenuDrop(self.frame, values=question_type_options, initial_value=question_type_options[0],
                                  width=40)
        self.submit_button = CustomButton(self.frame, text="Start", padding=BUTTON_PADDING, bg=BUTTON_BG, fg=BUTTON_FG,
                                          hover_fg=BUTTON_HOVER_FG, hover_bg=BUTTON_HOVER_BG,
                                          command=self.get_selected_values)

    # Function to retrieve and print values
    def get_selected_values(self):
        category = self.category_drop.get_value()
        difficulty = self.difficulty_drop.get_value()
        question_type = self.type_drop.get_value()
        amount = self.amount_drop.get_value()
        # print(f"Category: {category}, Difficulty: {difficulty}, Type: {question_type}, Amount: {amount}")
        questions = get_data(amount=amount, category=category, difficulty=difficulty,
                             question_type=question_type)
        self.on_retrieve_questions(questions)


