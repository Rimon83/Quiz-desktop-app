import html
import math
import random
from tkinter import *

from button_component import CustomButton
from canvas_component import CustomCanvas
from label_component import CustomLabel
from text_component import CustomText

# constant
BG_SIDE_BAR_FRAME = "#CAE0BC"
BG_SCREEN = "#EAFAEA"

# no questions exist label style
no_questions_label = {
    "padding": (5, 5),
    "font": ("Arial", 12),
    "bg_color": BG_SCREEN,
    "fg_color": "#780C28"

}


# question number label style
quiz_question_number_label = {
    "padding": (5, 5),
    "font": ("Arial", 12),
    "bg_color": BG_SCREEN,
    "fg_color": "#780C28",

}

# score label style
quiz_question_label = {
    "padding": (5, 5),
    "font": ("Arial", 24),
    "bg_color": BG_SCREEN,
    "fg_color": "#780C28",
    "anchor": "center"

}

# start button style
BUTTON_PADDING = (5, 5)
BUTTON_BG = "#780C28"
BUTTON_FG = "#CAE0BC"
BUTTON_HOVER_BG = "#CAE0BC"
BUTTON_HOVER_FG = "#780C28"


class QuestionUi:
    def __init__(self, parent, questions):
        self.choice_text = None
        self.current_index = 0
        self.questions = questions
        self.choices = []
        self.choice_widgets = []
        self.score = 0
        self.parent = parent
        self.reset()

        self.sub_frame = Frame(parent)
        self.sub_frame.pack(fill="both", side="top", padx=20)
        self.sub_frame.config(bg=BG_SCREEN)

        self.not_found_questions_label = CustomLabel(parent,
                                                     text="",
                                                     padding=no_questions_label["padding"],
                                                     font=no_questions_label["font"],
                                                     bg=no_questions_label["bg_color"],
                                                     fg=no_questions_label["fg_color"])

        self.show_result = None
        # question number frame
        self.question_number_frame = Frame(self.sub_frame)
        self.question_number_frame.config(bg=BG_SCREEN)
        self.question_number_frame.pack(side="left", expand=False)
        self.question_number_label = CustomLabel(self.question_number_frame,
                                                 text="",
                                                 padding=quiz_question_number_label["padding"],
                                                 font=quiz_question_number_label["font"],
                                                 bg=quiz_question_number_label["bg_color"],
                                                 fg=quiz_question_number_label["fg_color"])

        # score label frame
        score_frame = Frame(self.sub_frame)
        score_frame.config(bg=BG_SCREEN)
        score_frame.pack(side="right", expand=False)

        self.score_label = CustomLabel(score_frame,
                                       text="",
                                       padding=quiz_question_number_label["padding"],
                                       font=quiz_question_number_label["font"],
                                       bg=quiz_question_number_label["bg_color"],
                                       fg=quiz_question_number_label["fg_color"])

        self.question_canvas = CustomCanvas(parent, width=600, height=200, bg=BG_SCREEN)
        self.canvas_text = self.question_canvas.create_canvas_text(x_coor=300, y_coor=100, text="",
                                                                   font=("Arial", 20, "italic"),
                                                                   width=600)

        self.choices_frame = Frame(parent, bg=BG_SCREEN, padx=20, pady=20)
        self.choices_frame.pack()

        self.next_button_frame = Frame(parent, padx=20, bg=BG_SCREEN)
        self.next_button_frame.pack(side="right")

        # next button
        self.next_button = CustomButton(self.next_button_frame, text="Next", padding=BUTTON_PADDING, bg=BUTTON_BG,
                                        fg=BUTTON_FG,
                                        hover_fg=BUTTON_HOVER_FG, hover_bg=BUTTON_HOVER_BG,
                                        command=self.get_next_question)
        self.next_button.hide_button()

        self.initial_question()

    def get_next_question(self):
        self.clear_frame_widgets(self.choices_frame)

        self.current_index += 1
        if self.current_index < len(self.questions):
            self.question_canvas.itemconfig(self.canvas_text,
                                            text=html.unescape(self.questions[self.current_index]["question"]))
            self.question_number_label.set_label(f"{self.current_index + 1}/{len(self.questions)}")
            choices = self.questions[self.current_index]["incorrect_answers"]
            random_index = random.randint(0, len(choices) - 1)
            choices.insert(random_index, self.questions[self.current_index]["correct_answer"])
            for index, choice in enumerate(choices):
                self.choice_text = CustomText(self.choices_frame, width=40, height=2, font=("Arial", 12),
                                              pady=10,
                                              cursor="hand2")
                self.choice_widgets.append(self.choice_text)
                self.choice_text.insert_value(html.unescape(choice))
                self.choice_text.center_value()
                self.choice_text.handle_click(self.handle_correct_answer)
                self.choice_text.disable_text()
        if self.current_index == len(self.questions) - 1:
            self.next_button.hide_button()
        self.next_button.disable_button()

    """clear all widget in frame"""

    def clear_frame_widgets(self, frame_name):
        for widget in frame_name.winfo_children():  # Remove old widgets
            widget.destroy()

    def handle_correct_answer(self, selected_choice):
        """Handle when a user selects an answer."""
        self.next_button.enable_button()
        for choice in self.choice_widgets:
            choice.disable_click()  # Disable all choices

        selected_answer = selected_choice.get_text_value()
        correct_answer = html.unescape(self.questions[self.current_index]["correct_answer"])

        if selected_answer == correct_answer:
            selected_choice.mark_correct()  # Mark green if correct
            self.score += 1
            self.score_label.set_label(f"Score: {self.score}")

        else:
            selected_choice.mark_incorrect()  # Mark red if incorrect
            # Highlight the correct choice in green
            for choice in self.choice_widgets:
                if choice.get_text_value() == correct_answer:
                    choice.mark_correct()
        self.choice_widgets = []
        self.show_result_test()

    def initial_question(self):
        self.not_found_questions_label.set_label("")
        self.clear_frame_widgets(self.choices_frame)

        if len(self.questions) == 0:
            self.not_found_questions_label.set_label("Sorry there are no questions matched, change the setting test")
            return

        self.question_number_label.set_label(f"{self.current_index + 1}/{len(self.questions)}")
        self.score_label.set_label(f"Score: {0}")
        self.question_canvas.itemconfig(self.canvas_text,
                                        text=html.unescape(self.questions[self.current_index]["question"]))
        choices = self.questions[self.current_index]["incorrect_answers"]
        random_index = random.randint(0, len(choices) - 1)
        choices.insert(random_index, self.questions[self.current_index]["correct_answer"])
        for index, choice in enumerate(choices):
            choice_text = CustomText(self.choices_frame, width=40, height=2, font=("Arial", 12), pady=10,
                                     cursor="hand2")
            self.choice_widgets.append(choice_text)
            choice_text.insert_value(html.unescape(choice))
            choice_text.center_value()
            choice_text.handle_click(self.handle_correct_answer)
            choice_text.disable_text()

        self.next_button.show_button()
        self.next_button.disable_button()

    """"reset the values when start new test"""

    def reset(self):
        self.current_index = 0
        self.score = 0
        self.choice_widgets = []
        self.clear_frame_widgets(self.parent)

    """Show result at the end of test"""

    def show_result_test(self):
        if self.current_index == len(self.questions) - 1:
            result = math.floor((self.score / len(self.questions)) * 100)
            self.show_result = CustomLabel(self.parent,
                                           text="",
                                           padding=no_questions_label["padding"],
                                           font=no_questions_label["font"],
                                           bg=no_questions_label["bg_color"],
                                           fg=no_questions_label["fg_color"])
            if self.score > 60:
                self.show_result.set_label(f"Congratulation! 🙂 You pass the test with {result}%")
            else:
                self.show_result.set_label(f"Sorry!😔 You Failed the test with {result}%")
