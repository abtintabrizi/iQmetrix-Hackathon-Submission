import tkinter as tk             
from tkinter import font as tkfont

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold")

        self.frames = {}
        for F in (StartPage, EmployerPage, EmployeePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="light blue")
        label = tk.Label(self, text="Employee Database", font=controller.title_font, bg="light blue")
        label.pack(side="top", pady=75)

        button1 = tk.Button(self, text="Log In", width=40, height=4, bg="royal blue", borderwidth=0,
                            command=lambda: controller.show_frame("EmployerPage"))
        button2 = tk.Button(self, text="Sign Up", width=40, height=4, bg="royal blue", borderwidth=0,
                            command=lambda: controller.show_frame("EmployeePage"))
        button1.pack(pady=(0, 75))
        button2.pack()


class EmployerPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="light blue")
        button = tk.Button(self, text="Log Out", width=10, height=2, bg="royal blue", borderwidth=0,
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class EmployeePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="light blue")
        button = tk.Button(self, text="Log Out", width=10, height=2, bg="royal blue", borderwidth=0,
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.geometry("1280x720")
    app.title("Employee Database")
    app.resizable(False, False)
    app.mainloop()