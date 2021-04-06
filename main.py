import tkinter as tk
from tkinter import font as tkfont
from tkinter import filedialog, asksaveasfile


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.title_font = tkfont.Font(
            family='Helvetica', size=18, weight="bold")

        self.frames = {}
        for F in (StartPage, EmployerPage, EmployeePage, ViewFilesPage, AddFilePage):
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
        label = tk.Label(self, text="Employee Database",
                         font=controller.title_font, bg="light blue")
        label.place(anchor="n", relx=0.5, rely=0.05)
        button1 = tk.Button(self, text="Employer", width=40, height=4, bg="royal blue", borderwidth=0,
                            command=lambda: controller.show_frame("EmployerPage"))
        button2 = tk.Button(self, text="Employee", width=40, height=4, bg="royal blue", borderwidth=0,
                            command=lambda: controller.show_frame("EmployeePage"))
        button1.place(relwidth=0.5, relheight=0.25, relx=0.25, rely=0.25)
        button2.place(relwidth=0.5, relheight=0.25, relx=0.25, rely=0.6)


class EmployerPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="light blue")
        button = tk.Button(self, text="Log Out", bg="royal blue", borderwidth=0,
                           command=lambda: controller.show_frame("StartPage"))
        button.place(relheight=0.1, relwidth=0.1)


class EmployeePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="light blue")
        button = tk.Button(self, text="Log Out", bg="royal blue", borderwidth=0,
                           command=lambda: controller.show_frame("StartPage"))
        button.place(relheight=0.1, relwidth=0.1)
        title = tk.Label(self, text="Profile",
                         font=controller.title_font, bg="light blue")
        title.place(relx=0.5, rely=0.05)
        offerHistoryButton = tk.Button(self, text="Offer History", bg="royal blue", borderwidth=0,
                                       command=lambda: controller.show_frame("StartPage"))
        offerHistoryButton.place(
            relwidth=0.25, relheight=0.33, relx=0.1, rely=0.33)
        skillsProfileButton = tk.Button(self, text="Skills Profile", bg="royal blue", borderwidth=0,
                                        command=lambda: controller.show_frame("StartPage"))
        skillsProfileButton.place(
            relwidth=0.25, relheight=0.33, relx=0.4, rely=0.33)
        viewFilesButton = tk.Button(self, text="View Files", bg="royal blue", borderwidth=0,
                                    command=lambda: controller.show_frame("ViewFilesPage"))
        viewFilesButton.place(
            relwidth=0.25, relheight=0.33, relx=0.7, rely=0.33)


class ViewFilesPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="light blue")
        button = tk.Button(self, text="Back", bg="royal blue", borderwidth=0,
                           command=lambda: controller.show_frame("EmployeePage"))
        button.place(relheight=0.1, relwidth=0.1)
        title = tk.Label(self, text="View Files",
                         font=controller.title_font, bg="light blue")
        title.place(relx=0.5, rely=0.05)
        addFileButton = tk.Button(self, text="Add File", bg="royal blue", borderwidth=0,
                                  command=lambda: controller.show_frame("AddFilePage"))
        addFileButton.place(relx=0.45, rely=0.8, relwidth=0.2, relheight=0.1)


class AddFilePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="light blue")
        button = tk.Button(self, text="Back", bg="royal blue", borderwidth=0,
                           command=lambda: controller.show_frame("ViewFilesPage")).place(relheight=0.1, relwidth=0.1)
        title = tk.Label(self, text="Add File", font=controller.title_font,
                         bg="light blue").place(relx=0.5, rely=0.05)
        tk.Label(self, text="Upload", font=controller.title_font,
                 bg="light blue").place(relx=0.35, rely=0.35)
        uploadButton = tk.Button(self, text="Upload", bg="royal blue", borderwidth=0,
                                 command=self.get).place(relx=0.45, rely=0.8, relwidth=0.2, relheight=0.1)
        attachButton = tk.Button(self, text="Attach", bg="royal blue", borderwidth=0,
                                 command=self.attachAction).place(relx=0.45, rely=0.5, relwidth=0.2, relheight=0.1)

        self.name = tk.Entry(self)
        self.name.place(relx=0.5, rely=0.35)

    def get(self):
        print(self.name.get())

    def attachAction(event=None):
        filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("Text files", "*.txt*"), ("all files","*.*")))
        print(filename)


if __name__ == "__main__":
    app = SampleApp()
    app.geometry("1280x720")
    app.title("Employee Database")
    app.resizable(False, False)
    app.mainloop()
