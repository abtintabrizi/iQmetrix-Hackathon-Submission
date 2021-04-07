import tkinter as tk
from tkinter import font as tkfont
from tkinter import filedialog, Canvas
from sqlit

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
        for F in (StartPage, EmployerPage, EmployeePage, ViewFilesPage, AddFilePage, SentOffersPage, FilterPage, SkillsProfilePage):
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
        title = tk.Label(self, text="Employee Database",
                         font=controller.title_font, bg="light blue")
        title.place(x=600, y=70)
        log_out = tk.Button(self, text="Exit", width=10, height=2, bg="royal blue", borderwidth=0,
                            command=lambda: controller.show_frame("StartPage"))
        log_out.grid(row=0, column=0)
        sent_offers = tk.Button(self, text="Sent Offers", width=10, height=2, bg="royal blue", borderwidth=0,
                                command=lambda: controller.show_frame("SentOffersPage"))
        sent_offers.place(x=1205, y=0)
        filter_bt = tk.Button(self, text="Filter", width=10, height=2, bg="royal blue", borderwidth=0,
                            command=lambda: controller.show_frame("FilterPage"))
        filter_bt.place(x=100, y=80)


class SentOffersPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg = "light blue")
        back = tk.Button(self, text="Back", width=10, height=2, bg="royal blue", borderwidth=0,
                            command=lambda: controller.show_frame("EmployerPage"))
        back.grid(row=0, column=0)


class FilterPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg = "light blue")
        back = tk.Button(self, text="Back", width=10, height=2, bg="royal blue", borderwidth=0,
                            command=lambda: controller.show_frame("EmployerPage"))
        back.grid(row=0, column=0)


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
                                        command=lambda: controller.show_frame("SkillsProfilePage"))
        skillsProfileButton.place(
            relwidth=0.25, relheight=0.33, relx=0.4, rely=0.33)
        viewFilesButton = tk.Button(self, text="View Files", bg="royal blue", borderwidth=0,
                                    command=lambda: controller.show_frame("ViewFilesPage"))
        viewFilesButton.place(
            relwidth=0.25, relheight=0.33, relx=0.7, rely=0.33)


fileList = []

class ViewFilesPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="light blue")
        canvas = Canvas(self)
        canvas.configure(bg="light blue", highlightthickness=0)
        canvas.create_line(25, 80, 500, 80)
        canvas.create_line(225, 25, 225, 900)
        canvas.place(relx=0.37, rely=0.2, relwidth=0.35, relheight=0.5)
        button = tk.Button(self, text="Back", bg="royal blue", borderwidth=0,
                           command=lambda: controller.show_frame("EmployeePage"))
        button.place(relheight=0.1, relwidth=0.1)
        title = tk.Label(self, text="View Files",
                         font=controller.title_font, bg="light blue")
        title.place(relx=0.5, rely=0.05)
        addFileButton = tk.Button(self, text="Add File", bg="royal blue", borderwidth=0,
                                  command=lambda: controller.show_frame("AddFilePage"))
        addFileButton.place(relx=0.45, rely=0.8, relwidth=0.2, relheight=0.1)
        tk.Label(self, text="File Name", font=controller.title_font, bg="light blue").place(relx=0.43, rely=0.25)
        tk.Label(self, text="Download", font=controller.title_font, bg="light blue").place(relx=0.57, rely=0.25)
        refreshButton = tk.Button(self, text="refresh", width=10, height=2, bg="royal blue", borderwidth=0,
                                command=self.refresh)
        refreshButton.place(x=1205, y=0)

    def refresh(self):
        y = 0.35
        for x in range(len(fileList)):
            tk.Label(self, text=fileList[x], bg="light blue").place(relx=0.45, rely=y)
            tk.Button(self, text="Download", bg="white", borderwidth=0).place(relx=0.57, rely=y, relwidth=0.1, relheight=0.05)
            y = y + 0.1
        

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
        self.name.place(relx=0.45, rely=0.33, relwidth=0.2, relheight=0.1)

    def get(self):
        filename = self.name.get()
        fileList.append(filename)

    def attachAction(event=None):
        filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("Text files", "*.txt*"), ("all files","*.*")))


class SkillsProfilePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="light blue")
        button = tk.Button(self, text="Back", bg="royal blue", borderwidth=0,
                           command=lambda: controller.show_frame("EmployeePage")).place(relheight=0.1, relwidth=0.1)
        title = tk.Label(self, text="Skills Profile", font=controller.title_font,
                         bg="light blue").place(relx=0.5, rely=0.05)
        uploadButton = tk.Button(self, text="Upload", bg="royal blue", borderwidth=0).place(relx=0.45, rely=0.8, relwidth=0.2, relheight=0.1)
        tk.Label(self, text="Name", font=controller.title_font,
                 bg="light blue").place(relx=0.35, rely=0.35)
        tk.Label(self, text="City", font=controller.title_font,
                 bg="light blue").place(relx=0.35, rely=0.45)
        tk.Label(self, text="jobs", font=controller.title_font,
                 bg="light blue").place(relx=0.35, rely=0.55)
        self.name = tk.Entry(self)
        self.name.place(relx=0.45, rely=0.33, relwidth=0.2, relheight=0.1)
        self.city = tk.Entry(self)
        self.city.place(relx=0.45, rely=0.43, relwidth=0.2, relheight=0.1)
        self.job = tk.Entry(self)
        self.job.place(relx=0.45, rely=0.53, relwidth=0.2, relheight=0.1)


class Employee:
    def __init__(self, name, city, job):
        self.name = name
        self.city = city
        self.job = job

if __name__ == "__main__":
    app = SampleApp()
    app.geometry("1280x720")
    app.title("Employee Database")
    app.resizable(False, False)
    app.mainloop()
