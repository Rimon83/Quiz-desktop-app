import tkinter

#constants
GREEN = "#A9C46C"
RED = "#EB5A3C"


class CustomText(tkinter.Text):
    def __init__(self, parent, **kwargs):
        self.font = kwargs.get("font", ("arial", 10, "normal"))
        self.bg = kwargs.get("bg", "white")
        self.fg = kwargs.get("fg", "black")
        self.width = kwargs.get("width", 10)
        self.height = kwargs.get("height", 0)
        self.padx = kwargs.get("padx", 10)
        self.pady = kwargs.get("pady", 10)
        self.cursor = kwargs.get("cursor")
        self.clickable = True  # Keep track of whether choices can be clicked
        super().__init__(parent, width=self.width, height=self.height, font=self.font, bg=self.bg, fg=self.fg,
                         cursor=self.cursor)

        """ use grid """
        # self.row = kwargs.get("row", 0)
        # self.column = kwargs.get("column", 0)
        # self.columnspan = kwargs.get("columnspan", 1)
        # self.grid(row=self.row, column=self.column, columnspan=self.columnspan, padx=self.padx, pady=self.pady)
        self.pack(fill="x", padx=self.padx, pady=self.pady)

    # disable the text
    def disable_text(self):
        self.config(state="disabled")

    # insert value
    def insert_value(self, new_value):
        self.insert("end", new_value)

    """center the value in text"""

    def center_value(self):
        self.tag_config("center", justify="center")
        self.tag_add("center", "1.0", "end")

    def get_text_value(self):
        return self.get("1.0", "end").strip()

    """hide the text widget"""

    def hide_text_tag(self):
        self.pack_forget()

    """show text widget"""

    def show_text_tag(self):
        self.pack(fill="x", padx=self.padx, pady=self.pady)

    def handle_click(self, on_click):
        self.bind("<Button-1>", lambda event: on_click(self))

    """Change background to green for correct answer."""

    def mark_correct(self):
        self.config(bg=GREEN)

    """Change background to red for incorrect answer."""

    def mark_incorrect(self):
        self.config(bg=RED)

    """Disable the widget from being clicked again."""

    def disable_click(self):
        self.unbind("<Button-1>")
