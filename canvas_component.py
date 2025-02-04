import tkinter


class CustomCanvas(tkinter.Canvas):
    def __init__(self, parent, **kwargs):
        self.frame2 = None
        self.width = kwargs.get("width", 100)
        self.height = kwargs.get("height")
        self.bg = kwargs.get("bg")
        self.highlightthickness = kwargs.get("highlightthickness", 0)
        super().__init__(parent, width=self.width, height=self.height,
                         bg=self.bg, highlightthickness=self.highlightthickness)
        self.pack()

    def create_canvas_image(self, x_coor, y_coor, image):
        return self.create_image(x_coor, y_coor, image=image)

    def create_canvas_text(self, x_coor, y_coor, **kwargs ):
        return self.create_text(x_coor, y_coor, text=kwargs.get("text", ""), font=kwargs.get("font"),
                                width=kwargs.get("width"))

    def update_scroll_region(self, event=None):
        """Updates the scroll region of the canvas"""
        self.configure(scrollregion=self.bbox("all"))

    def create_scrollbar_grid(self, frame_name):
        self.frame2 = frame_name
        """Creates a scrollbar and a scrollable frame inside the canvas"""
        # Create vertical scrollbar
        scrollbar = tkinter.Scrollbar(self.parent, orient="vertical", command=self.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")

        # Configure canvas to use the scrollbar
        self.configure(yscrollcommand=scrollbar.set)

        self.create_window((0, 0), window=self.frame2, anchor="nw")

        # Bind frame resizing to update scroll region
        self.frame2.bind("<Configure>", lambda event: self.update_scroll_region())

        # Expand `canvas` within `parent`
        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)


# import tkinter
#
#
# class CanvasComponent(tkinter.Canvas):
#     def __init__(self, parent, **kwargs):
#         self.frame2 = None
#         self.width = kwargs.get("width", 100)
#         self.height = kwargs.get("height")
#         self.parent = parent
#         self.bg = kwargs.get("bg")
#         self.highlightthickness = kwargs.get("highlightthickness", 0)
#         super().__init__(parent, width=self.width, height=self.height,
#                          bg=self.bg, highlightthickness=self.highlightthickness)
#         self.row = kwargs.get("row", 0)
#         self.column = kwargs.get("column", 0)
#         self.columnspan = kwargs.get("columnspan", 1)
#         self.sticky = "nesw"
#         self.grid(row=self.row, column=self.column, columnspan=self.columnspan, sticky=self.sticky)
#
#     def create_canvas_image(self, x_coor, y_coor, image):
#         return self.create_image(x_coor, y_coor, image=image)
#
#     def create_canvas_text(self, x_coor, y_coor, **kwargs ):
#         return self.create_text(x_coor, y_coor, text=kwargs.get("text", ""), font=kwargs.get("font"))
#
#     def update_scroll_region(self, event=None):
#         """Updates the scroll region of the canvas"""
#         self.configure(scrollregion=self.bbox("all"))
#
#     def create_scrollbar_grid(self, frame_name):
#         self.frame2 = frame_name
#         """Creates a scrollbar and a scrollable frame inside the canvas"""
#         # Create vertical scrollbar
#         scrollbar = tkinter.Scrollbar(self.parent, orient="vertical", command=self.yview)
#         scrollbar.grid(row=0, column=1, sticky="ns")
#
#         # Configure canvas to use the scrollbar
#         self.configure(yscrollcommand=scrollbar.set)
#
#         self.create_window((0, 0), window=self.frame2, anchor="nw")
#
#         # Bind frame resizing to update scroll region
#         self.frame2.bind("<Configure>", lambda event: self.update_scroll_region())
#
#         # Expand `canvas` within `parent`
#         self.parent.grid_rowconfigure(0, weight=1)
#         self.parent.grid_columnconfigure(0, weight=1)