#use ttk
from tkinter import ttk, StringVar

#constant
PADDING_X = 20
PADDING_Y = 40


class CustomButton(ttk.Button):
    def __init__(self, parent, **kwargs):
        self.text_var = StringVar()
        self.text_var.set(kwargs.get("text", "Label"))
        self.font = kwargs.get("font", ("arial", 12, "normal"))
        self.bg = kwargs.get("bg", "white")
        self.fg = kwargs.get("fg", "black")
        self.width = kwargs.get("width")
        self.highlightthickness = kwargs.get("highlightthickness", 0)
        self.image = kwargs.get("image")
        self.command = kwargs.get("command")
        self.padding = kwargs.get("padding", (2, 2))
        self.hover_fg = kwargs.get("hover_fg")
        self.hover_bg = kwargs.get("hover_bg")

        # style the button
        # Create a unique style name based on instance ID
        self.style_name = f"CustomLabel{str(id(self))}.TButton"
        self.style = ttk.Style()

        # Configure the style
        self.style.configure(self.style_name,
                             font=self.font,
                             foreground=self.fg,
                             background=self.bg,
                             padding=self.padding)
        self.style.map(self.style_name,
                       background=[("active", self.hover_bg)],
                       foreground=[("active", self.hover_fg)]
                       )
        super().__init__(parent, style=self.style_name, textvariable=self.text_var, image=self.image, width=self.width,
                         command=self.command, cursor="hand2")
        self.pack(fill="x", padx=PADDING_X, pady=PADDING_Y)

    def edit_text_button(self, new_button_text):
        self.text_var.set(new_button_text)

    # hide the button
    def hide_button(self):
        self.pack_forget()

    # show button
    def show_button(self):
        self.pack(fill="x", padx=PADDING_X, pady=PADDING_Y)

    # disable the button
    def disable_button(self):
        self.config(state="disabled")

    def enable_button(self):
        self.config(state="enabled")





# using tkinter

# import tkinter
#
#
# class ButtonComponent(tkinter.Button):
#     def __init__(self, parent, **kwargs):
#         self.text_var = tkinter.StringVar()
#         self.text_var.set(kwargs.get("text", "Label"))
#         self.font = kwargs.get("font", ("arial", 10, "normal"))
#         self.bg = kwargs.get("bg", "white")
#         self.fg = kwargs.get("fg", "black")
#         self.width = kwargs.get("width")
#         self.highlightthickness = kwargs.get("highlightthickness", 0)
#         self.image = kwargs.get("image")
#         self.command = kwargs.get("command")
#         super().__init__(parent, textvariable=self.text_var, image=self.image, width=self.width, font=self.font, bg=self.bg, fg=self.fg,
#                          highlightthickness=self.highlightthickness, command=self.command)
#         self.row = kwargs.get("row", 0)
#         self.column = kwargs.get("column", 0)
#         self.columnspan = kwargs.get("columnspan", 1)
#         self.grid(row=self.row, column=self.column, columnspan=self.columnspan)
#
#     def edit_text_button(self, new_button_text):
#         self.text_var.set(new_button_text)
