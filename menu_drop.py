from tkinter import ttk, StringVar

# constant
PADDING_X = 20
PADDING_Y = 20
FONT = ('Arial', 12)
BG_OPTION_MENU = "#EAFAEA"
FOREGROUND_NOT_SELECTED_TEXT = "gray"
FOREGROUND_SELECTED_TEXT = "black"


class MenuDrop(ttk.Combobox):
    def __init__(self, parent, **kwargs):  # Fix constructor name
        self.options = kwargs.get("values", [])  # Default to empty list if no values
        self.selected_value = StringVar()
        self.width = kwargs.get("width", 20)

        super().__init__(parent, textvariable=self.selected_value,
                         values=self.options,
                         state="readonly",
                         font=FONT,
                         width=self.width)
        self.set(kwargs.get("initial_value"))
        # styling
        self.style = ttk.Style()
        self.style.theme_use("clam")  # Use a modern theme like 'clam', 'alt', 'default', etc.
        self.style.configure("TCombobox", padding=(5, 5))

        self.style.map("TCombobox", fieldbackground=[("readonly", BG_OPTION_MENU)],  # Background when read-only
                       selectbackground=[("readonly", BG_OPTION_MENU)],  # Background when select item
                       selectforeground=[("readonly", "black")],  # Text color when select item
                       foreground=[("readonly", "gray")],  # text color when not select item
                       background=[("readonly", BG_OPTION_MENU)],  # Background color of the dropdown button

                       )

        self.pack(fill="x", padx=PADDING_X, pady=PADDING_Y)
        self.selected_value.trace_add("write", self.on_selection)
        # self.frame.bind("<Configure>", self.update_combobox_width)

    # Function to track changes
    def on_selection(self, *args):
        print(f"Selected: {self.selected_value.get()}")

    def get_value(self):
        """Returns the current selected value."""
        return self.selected_value.get()

    # def update_combobox_width(self, event=None):  # Accept `event` parameter
    #     window_width = self.root.winfo_width()  # Get the current window width
    #     new_width = max(15, window_width // 30)  # Adjust width dynamically
    #     self.config(width=new_width)  # Update combobox width
