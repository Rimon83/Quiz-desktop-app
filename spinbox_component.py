from tkinter import ttk, StringVar

PADDING_X = 20
PADDING_Y = 20
FONT = ('Arial', 12)
BG_OPTION_MENU = "#EAFAEA"
FOREGROUND_NOT_SELECTED_TEXT = "gray"
FOREGROUND_SELECTED_TEXT = "black"
PADDING = (5, 5)


class CustomSpinbox(ttk.Spinbox):
    def __init__(self, parent, **kwargs):
        self.from_value = kwargs.get("from_value", 1)
        self.to_value = kwargs.get("to_value", 10)
        self.increment = kwargs.get("increment", 1.0)
        self.wrap = kwargs.get("wrap", False)  # Boolean flag
        self.selected_value = StringVar()
        self.width = kwargs.get("width", 20)

        super().__init__(parent, from_=self.from_value, to=self.to_value,
                         increment=self.increment, wrap=self.wrap,
                         textvariable=self.selected_value, state="readonly", width=self.width)
        self.set(1)
        # styling
        self.style = ttk.Style()
        self.style.theme_use("clam")  # Use a modern theme like 'clam', 'alt', 'default', etc.
        self.style.configure("TSpinbox", padding=PADDING)

        self.style.map("TSpinbox", fieldbackground=[("readonly", BG_OPTION_MENU)],  # Background when read-only
                       selectbackground=[("readonly", BG_OPTION_MENU)],  # Background when select item
                       selectforeground=[("readonly", "black")],  # Text color when select item
                       foreground=[("readonly", "gray")],  # text color when not select item
                       background=[("readonly", BG_OPTION_MENU)],  # Background color of the dropdown button

                       )

        self.pack(fill="x", padx=PADDING_X, pady=PADDING_Y)

    def get_value(self):
        """Returns the current spinbox value."""
        return self.selected_value.get()
