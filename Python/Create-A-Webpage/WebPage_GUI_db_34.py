from tkinter import *
from tkinter import ttk
import webbrowser
import sqlite3
import time
import os

content = """<html>
<body>\n\n\n
</body>
</html>"""

conn = sqlite3.connect("WebContent.db")
c = conn.cursor()

class Feedback:
    def __init__(self, master):
        master.title("Generate a Webpage")
        master.configure(background = "#CB8F8F")

        self.style = ttk.Style()
        self.style.configure("TFrame", background = "#CB8F8F")
        self.style.configure("TButton", background = "#CB8F8F")

        #Menu
        master.option_add("*tearOff", False)
        self.menubar = Menu(master)
        master.config(menu = self.menubar)
        self.file = Menu(self.menubar)
        self.menubar.add_cascade(menu = self.file, label = "File")
        self.file.add_command(label = "New", command = self.newPage)
        self.file.add_command(label = "Open", command = self.openPage)
        self.file.add_command(label = "Save", command = self.save)
        self.file.add_command(label = "Save As", command = self.saveAsPage)
        self.file.add_command(label = "Exit", command = lambda: master.destroy())

        #Frame 1
        self.frame1 = ttk.Frame(master)
        self.frame1.pack(pady = 10)

        ttk.Label(self.frame1, text = "URL:",
                  background = "#CB8F8F").grid(row = 0, column = 0, sticky = "w")
        self.label2 = StringVar()
        ttk.Label(self.frame1, textvariable = self.label2,
                  background = "#CB8F8F").grid(row = 0, column = 1, sticky = "w")

        #Frame 2
        self.frame2 = ttk.Frame(master)
        self.frame2.pack(padx = 10)

        self.text = Text(self.frame2, width = 60, height = 15, state = DISABLED,
                font = ("Arial", 10), bg = "#E9E3E3")
        self.text.pack(side = LEFT, fill = BOTH)

        self.scroll = ttk.Scrollbar(self.frame2, orient = VERTICAL,
                command = self.text.yview)
        self.scroll.pack(side = RIGHT, fill = Y)
        self.text.config(yscrollcommand = self.scroll.set)

        #Frame 3
        self.frame3 = ttk.Frame(master)
        self.frame3.pack(pady = 10)

        ttk.Button(self.frame3, text = "Load in Broswer",
                command = self.loadPage).grid(row = 0, column = 0, padx = 5)
        ttk.Button(self.frame3, text = "Save",
                command = self.save).grid(row = 0, column = 1, padx = 5)

    def newPage(self):
        time.sleep(0.5)
        self.text.delete("1.0", "end")
        self.label2.set("UNTITLED")
        self.text.config(state = NORMAL)
        self.text.insert("1.0", content)

    def save(self):
        self.text.edit_modified(False)
        url = self.label2.get()
        if url == "UNTITLED":
            self.saveAsPage()
        else:
            content = self.text.get("1.0", "end")
            fullPath = os.path.realpath(url)
            file = open(fullPath, "w")
            file.write(content)
            file.close()

    def saveAsPage(self):
        url = self.label2.get()
        if url == "":
            messagebox.showerror("Error", "Create a new file or open an existing one.")
        else:
            content = self.text.get("1.0", "end")
            saPath = filedialog.asksaveasfilename(filetypes = [("HTML Files", "*.html")],
                    defaultextension = ".html", initialfile = "*.html")
            if not saPath:
                return
            else:
                file = open(saPath, "w")
                file.write(content)
                file.close()
                url = os.path.basename(saPath)
                self.label2.set(url)

                c.execute("CREATE TABLE if not exists WEBPAGE(ID INTEGER PRIMARY KEY, URL TEXT VARCHAR(255));")
                c.execute("INSERT INTO WEBPAGE (URL) VALUES ('{}');".format(saPath))
                conn.commit()

                self.text.edit_modified(False)

    def openPage(self):
        global readContent
        self.storedPages = Toplevel()
        self.storedPages.title("Select a Webpage")
        self.storedPages.config(bg = "#CB8F8F")
        self.frame = ttk.Frame(self.storedPages)
        self.frame.pack(padx = 10)
        self.style = ttk.Style()
        self.style.configure("Treeview", background = "#E9E3E3")
        self.treeview = ttk.Treeview(self.frame)
        self.treeview.pack(expand = True, fill = BOTH, pady = 10)
        self.treeview.config(columns = ("URL"))
        self.treeview.column("#0", width = 50, stretch = 0)
        self.treeview.column("URL", width = 350)
        self.treeview.heading("URL", text = "Webpage", anchor = 'w')

        c.execute("SELECT * FROM WEBPAGE;")
        rows = c.fetchall()
        for row in rows:
            idno = row[0]
            self.treeview.insert("", "end", idno, text = idno)
            self.treeview.set(idno, "URL", row[1])
            
        self.treeview.config(height = idno, selectmode = "browse")
        ttk.Button(self.frame, text = "Open", command = self.displayPage).pack(pady = 5)
        
    def displayPage(self):
        item = self.treeview.selection()
        getPath = self.treeview.set(item).get("URL")
        url = os.path.basename(getPath)
        self.label2.set(url)
        file = open(getPath, "r")
        content = file.read()
        file.close()
        self.text.config(state = NORMAL)
        self.text.delete("1.0", "end")
        self.text.insert("1.0", content)
        self.text.edit_modified(False)
        self.storedPages.destroy()
        
    def loadPage(self):
        url = self.label2.get()
        if url == "":
            messagebox.showerror("Error", "Create a new file or open an existing one.")
        elif url == "UNTITLED":
            self.saveAsPage()
        elif self.text.edit_modified() == True:
            saveOK = messagebox.askokcancel("Save File before Loading",
                    "Would you like to save this file?")
            if saveOK == True:
                content = self.text.get("1.0", "end")
                fullPath = os.path.realpath(url)
                file = open(fullPath, "w")
                file.write(content)
                file.close()
                self.text.edit_modified(False)
                time.sleep(0.5)
                webbrowser.open(url)
            else:
                return
        else:
            webbrowser.open(url)

def main():
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()

if __name__ == "__main__":main()

        
            
