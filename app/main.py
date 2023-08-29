import tkinter as tk
from tkinter import *


class MockItApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MockIt Interview Training App")
        self.left_frame = Frame(root, width=400, height=400)
        self.left_frame.grid(row=0, column=0, padx=10, pady=5)
        self.root.mainloop()

        self.create_ui()

    def create_ui(self):
        # Create Frame widget
        pass

    def start_session(self):
        # Start an interview session
        pass

    def save_video(self):
        # Save recorded video
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = MockItApp(root)
    root.mainloop()
