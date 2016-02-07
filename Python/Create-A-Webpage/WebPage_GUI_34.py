import webbrowser
from tkinter import *
from tkinter import ttk

url = "SummerSale.html"
contents = """<html>
<body>Stay tuned for our amazing summer sale!</body>
</html>"""

class Feedback:
    def __init__(self, master):

        master.title("Create HTML Page")
        master.configure(background = "#CB8F8F")

        self.style = ttk.Style()
        self.style.configure("TFrame", background = "#CB8F8F")
        self.style.configure("TButton", background = "#CB8F8F")
        
        
        self.frame1 = ttk.Frame(master)
        self.frame1.pack(pady = 10)

        
        ttk.Label(self.frame1, text = "Create a new URL or enter an existing URL:",
                background = "#CB8F8F").grid(row = 0, column = 0, sticky = "w")
        
        
        self.enterURL = Entry(self.frame1, text = "", width = 58,
                relief = SUNKEN, borderwidth = 2, bg = "#E9E3E3")
        self.enterURL.grid(row = 1, column = 0, padx = 5)
        ttk.Button(self.frame1, text = "Save URL",
                command = self.saveURL).grid(row = 1, column = 1, padx = 5)

        self.frame2 = ttk.Frame(master)
        self.frame2.pack()
        
        ttk.Label(self.frame2, text = "Edit the content of your page:",
                background = "#CB8F8F", width = 74).pack(side = LEFT)

        self.frame3 = ttk.Frame(master, relief = RAISED, borderwidth = 2)
        self.frame3.pack(padx = 10, pady = 10)

        self.bodyText = Text(self.frame3, width = 60, height = 15,
                font = ('Arial', 10), bg = "#E9E3E3")
        self.bodyText.pack(side = LEFT, fill = BOTH)
        self.bodyText.insert("1.0", contents)

        self.scroll = ttk.Scrollbar(self.frame3, orient = VERTICAL,
                command = self.bodyText.yview)
        self.scroll.pack(side = RIGHT, fill = Y)
        self.bodyText.config(yscrollcommand = self.scroll.set)

        self.frame4 = ttk.Frame(master)
        self.frame4.pack(pady = 10)
        
        ttk.Button(self.frame4, text = "Save Content",
                command = self.saveContent).grid(row = 0, column = 0, padx = 5)
        ttk.Button(self.frame4, text = "Load Page in Browser",
                command = self.loadWebPage).grid(row = 0, column = 1, padx = 5)

    def saveURL(self):
        global url
        #get URL from user
        url = self.enterURL.get()

    def saveContent(self):
        global contents
        #get text input from user
        contents = self.bodyText.get("1.0", "end")
        webPage = open(url, "w")
        webPage.write(contents)
        webPage.close()

    def loadWebPage(self):
        webbrowser.open(url)

def main():
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()

if __name__ == "__main__": main()
                        
