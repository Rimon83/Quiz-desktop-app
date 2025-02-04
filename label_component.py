""" use ttk """

from tkinter import ttk


class CustomLabel(ttk.Label):
    def __init__(self, parent, **kwargs):
        self.text = kwargs.get("text", "Label")
        self.font = kwargs.get("font", ("Arial", 12))
        self.fg = kwargs.get("fg", "black")
        self.bg = kwargs.get("bg", "white")
        self.padding = kwargs.get("padding", (2, 2))
        self.anchor = kwargs.get("anchor", "w")

        # Create a unique style name based on instance ID
        # self.style_name = f"CustomLabel{str(id(self))}.TLabel"

        # Initialize the ttk.Label with the custom style
        super().__init__(parent, text=self.text)
        self.config(font=self.font,
                    background=self.bg,
                    foreground=self.fg,
                    padding=self.padding,
                    anchor=self.anchor)

        # Pack with default options
        self.pack(padx=20, pady=15, fill="x")

    # set the value of label
    def set_label(self, value):
        self["text"] = value

    """hide the label"""
    def hide_label(self):
        self.pack_forget()

    """"show the label"""
    def show_label(self):
        self.pack(padx=20, pady=15, fill="x")



"""
use tkinter 
"""

# import tkinter
#
#
# class CustomLabel(tkinter.Label):
#     def __init__(self, parent, **kwargs):
#         self.text = kwargs.get("text", "Label")
#         self.font = kwargs.get("font", ("arial", 10, "normal"))
#         self.bg = kwargs.get("bg", "white")
#         self.fg = kwargs.get("fg", "black")
#         self.width = kwargs.get("width", 0)
#         self.height = kwargs.get("height", 0)
#         super().__init__(parent, text=self.text, width=self.width, height=self.height, font=self.font, bg=self.bg,
#                          fg=self.fg)
#         self.row = kwargs.get("row", 0)
#         self.column = kwargs.get("column", 0)
#         self.columnspan = kwargs.get("columnspan", 1)
#         self.grid(row=self.row, column=self.column, columnspan=self.columnspan)
#
#     def set_label(self, value):
#         self["text"] = value
