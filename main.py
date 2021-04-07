import sqlite3
import tkinter as tk
from tkinter import font as tkfont
from tkinter import filedialog, Canvas

conn = sqlite3.connect(':memory:')
c = conn.cursor()

c.execute("""CREATE TABLE employees (
            name text,
            city text,
            job text
            )""")

def insertEmp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:name, :city, :job)", {'name': emp.name, 'city': emp.city, 'job': emp.job})

def getEmpsByCity(city):
    c.execute("SELECT * FROM employees WHERE city=:city", {'city': city})
    return c.fetchall()

def getEmpsByJob(job):
    c.execute("SELECT * FROM employees WHERE job=:job", {'job': job})
    return c.fetchall()


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
        title.place(relx=0.4, rely=0.05)
        log_out = tk.Button(self, text="Exit", width=10, height=2, bg="royal blue", borderwidth=0,
                            command=lambda: controller.show_frame("StartPage"))
        log_out.grid(row=0, column=0)
        sent_offers = tk.Button(self, text="Sent Offers", width=10, height=2, bg="royal blue", borderwidth=0,
                                command=lambda: controller.show_frame("SentOffersPage"))
        sent_offers.place(x=1205, y=0)
        filter_bt = tk.Button(self, text="Filter", width=10, height=2, bg="royal blue", borderwidth=0,
                            command=lambda: controller.show_frame("FilterPage"))
        filter_bt.place(x=100, y=80)

        canvas = Canvas(self)
        canvas.configure(bg="light blue", highlightthickness=0)
        canvas.create_line(25, 80, 1050, 80)
        canvas.create_line(225, 25, 225, 900)
        canvas.create_line(400, 25, 400, 900)
        canvas.create_line(600, 25, 600, 900)
        canvas.create_line(820, 25, 820, 900)
        canvas.place(relx=0.08, rely=0.2, relwidth=1, relheight=1)
        tk.Label(self, text="Name", font=controller.title_font, bg="light blue").place(relx=0.15, rely=0.25)
        tk.Label(self, text="City", font=controller.title_font, bg="light blue").place(relx=0.30, rely=0.25)
        tk.Label(self, text="Job", font=controller.title_font, bg="light blue").place(relx=0.45, rely=0.25)
        tk.Label(self, text="Profile", font=controller.title_font, bg="light blue").place(relx=0.60, rely=0.25)
        tk.Label(self, text="Send Offer", font=controller.title_font, bg="light blue").place(relx=0.75, rely=0.25)

        self.city = tk.Entry(self)
        self.city.place(x=500, y=80, relwidth=0.15, relheight=0.05)
        self.job = tk.Entry(self)
        self.job.place(x=800, y=80, relwidth=0.15, relheight=0.05)
        filter_city = tk.Button(self, text="Filter City", width=10, height=2, bg="royal blue", borderwidth=0,
                                command=self.refreshCity)
        filter_city.place(x=400, y=80)
        filter_job = tk.Button(self, text="Filter Job", width=10, height=2, bg="royal blue", borderwidth=0,
                                command=self.refreshJob)
        filter_job.place(x=700, y=80)
        

    def refreshCity(self):
        self.clear()
        field = self.city.get()
        emps = getEmpsByCity(field) 
        y = 0.35
        for x in range(len(emps)):
            tk.Label(self, text=emps[x][0], bg="light blue").place(relx=0.15, rely=y)
            tk.Label(self, text=emps[x][1], bg="light blue").place(relx=0.30, rely=y)
            tk.Label(self, text=emps[x][2], bg="light blue").place(relx=0.45, rely=y)
            tk.Button(self, text="View", bg="white", borderwidth=0).place(relx=0.58, rely=y, relwidth=0.1, relheight=0.05)
            tk.Button(self, text="Send", bg="white", borderwidth=0).place(relx=0.75, rely=y, relwidth=0.1, relheight=0.05)
            y = y + 0.07

    def refreshJob(self):
        self.clear()
        field = self.job.get()
        emps = getEmpsByJob(field)
        y = 0.35
        for x in range(len(emps)):
            tk.Label(self, text=emps[x][0], bg="light blue").place(relx=0.15, rely=y)
            tk.Label(self, text=emps[x][1], bg="light blue").place(relx=0.30, rely=y)
            tk.Label(self, text=emps[x][2], bg="light blue").place(relx=0.43, rely=y)
            tk.Button(self, text="View", bg="white", borderwidth=0).place(relx=0.57, rely=y, relwidth=0.1, relheight=0.05)
            tk.Button(self, text="Send", bg="white", borderwidth=0).place(relx=0.75, rely=y, relwidth=0.1, relheight=0.05)
            y = y + 0.07

    def clear(self):
        canvas = Canvas(self)
        canvas.configure(bg="light blue", highlightthickness=0)
        canvas.create_line(25, 5, 1050, 5)
        canvas.create_line(225, 0, 225, 900)
        canvas.create_line(400, 0, 400, 900)
        canvas.create_line(600, 0, 600, 900)
        canvas.create_line(820, 0, 820, 900)
        canvas.place(relx=0.08, rely=0.3, relwidth=1, relheight=1)


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
        button = tk.Button(self, text="Exit", bg="royal blue", borderwidth=0,
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
        updateButton = tk.Button(self, text="Update", bg="royal blue", borderwidth=0, command=self.createEmp).place(relx=0.45, rely=0.8, relwidth=0.2, relheight=0.1)
        tk.Label(self, text="Name", font=controller.title_font,
                 bg="light blue").place(relx=0.35, rely=0.35)
        tk.Label(self, text="City", font=controller.title_font,
                 bg="light blue").place(relx=0.35, rely=0.45)
        tk.Label(self, text="Jobs", font=controller.title_font,
                 bg="light blue").place(relx=0.35, rely=0.55)
        self.name = tk.Entry(self)
        self.name.place(relx=0.45, rely=0.33, relwidth=0.2, relheight=0.1)
        self.city = tk.Entry(self)
        self.city.place(relx=0.45, rely=0.43, relwidth=0.2, relheight=0.1)
        self.job = tk.Entry(self)
        self.job.place(relx=0.45, rely=0.53, relwidth=0.2, relheight=0.1)

    def createEmp(self):
        name = self.name.get()
        city = self.city.get()
        job = self.job.get()
        emp = Employee(name, city, job)
        insertEmp(emp)


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


conn.close()
