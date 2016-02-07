from __future__ import absolute_import
from Tkinter import *
import ttk
import webbrowser
import sqlite3
import time
import os
from io import open

content = u"""<html>
<body>\n\n\n
</body>
</html>"""

conn = sqlite3.connect(u"WebContent.db")
c = conn.cursor()

class Feedback(object):
    def __init__(self, master):
        master.title(u"Generate a Webpage")
        master.configure(background = u"#CB8F8F")

        self.style = ttk.Style()
        self.style.configure(u"TFrame", background = u"#CB8F8F")
        self.style.configure(u"TButton", background = u"#CB8F8F")

        #Menu
        master.option_add(u"*tearOff", False)
        self.menubar = Menu(master)
        master.config(menu = self.menubar)
        self.file = Menu(self.menubar)
        self.menubar.add_cascade(menu = self.file, label = u"File")
        self.file.add_command(label = u"New", command = self.newPage)
        self.file.add_command(label = u"Open", command = self.openPage)
        self.file.add_command(label = u"Save", command = self.save)
        self.file.add_command(label = u"Save As", command = self.saveAsPage)
        self.file.add_command(label = u"Exit", command = lambda: master.destroy())

        #Frame 1
        self.frame1 = ttk.Frame(master)
        self.frame1.pack(pady = 10)

        ttk.Label(self.frame1, text = u"URL:",
                  background = u"#CB8F8F").grid(row = 0, column = 0, sticky = u"w")
        self.label2 = StringVar()
        ttk.Label(self.frame1, textvariable = self.label2,
                  background = u"#CB8F8F").grid(row = 0, column = 1, sticky = u"w")

        #Frame 2
        self.frame2 = ttk.Frame(master)
        self.frame2.pack(padx = 10)

        self.text = Text(self.frame2, width = 60, height = 15, state = DISABLED,
                font = (u"Arial", 10), bg = u"#E9E3E3")
        self.text.pack(side = LEFT, fill = BOTH)

        self.scroll = ttk.Scrollbar(self.frame2, orient = VERTICAL,
                command = self.text.yview)
        self.scroll.pack(side = RIGHT, fill = Y)
        self.text.config(yscrollcommand = self.scroll.set)

        #Frame 3
        self.frame3 = ttk.Frame(master)
        self.frame3.pack(pady = 10)

        ttk.Button(self.frame3, text = u"Load in Broswer",
                command = self.loadPage).grid(row = 0, column = 0, padx = 5)
        ttk.Button(self.frame3, text = u"Save",
                command = self.save).grid(row = 0, column = 1, padx = 5)

    def newPage(self):
        time.sleep(0.5)
        self.text.delete(u"1.0", u"end")
        self.label2.set(u"UNTITLED")
        self.text.config(state = NORMAL)
        self.text.insert(u"1.0", content)

    def save(self):
        self.text.edit_modified(False)
        url = self.label2.get()
        if url == u"UNTITLED":
            self.saveAsPage()
        else:
            content = self.text.get(u"1.0", u"end")
            fullPath = os.path.realpath(url)
            file = open(fullPath, u"w")
            file.write(content)
            file.close()

    def saveAsPage(self):
        url = self.label2.get()
        if url == u"":
            messagebox.showerror(u"Error", u"Create a new file or open an existing one.")
        else:
            content = self.text.get(u"1.0", u"end")
            saPath = filedialog.asksaveasfilename(filetypes = [(u"HTML Files", u"*.html")],
                    defaultextension = u".html", initialfile = u"*.html")
            if not saPath:
                return
            else:
                file = open(saPath, u"w")
                file.write(content)
                file.close()
                url = os.path.basename(saPath)
                self.label2.set(url)

                c.execute(u"CREATE TABLE if not exists WEBPAGE(ID INTEGER PRIMARY KEY, URL TEXT VARCHAR(255));")
                c.execute(u"INSERT INTO WEBPAGE (URL) VALUES ('{}');".format(saPath))
                conn.commit()

                self.text.edit_modified(False)

    def openPage(self):
        global readContent
        self.storedPages = Toplevel()
        self.storedPages.title(u"Select a Webpage")
        self.storedPages.config(bg = u"#CB8F8F")
        self.frame = ttk.Frame(self.storedPages)
        self.frame.pack(padx = 10)
        self.style = ttk.Style()
        self.style.configure(u"Treeview", background = u"#E9E3E3")
        self.treeview = ttk.Treeview(self.frame)
        self.treeview.pack(expand = True, fill = BOTH, pady = 10)
        self.treeview.config(columns = (u"URL"))
        self.treeview.column(u"#0", width = 50, stretch = 0)
        self.treeview.column(u"URL", width = 350)
        self.treeview.heading(u"URL", text = u"Webpage", anchor = u'w')

        c.execute(u"SELECT * FROM WEBPAGE;")
        rows = c.fetchall()
        for row in rows:
            idno = row[0]
            self.treeview.insert(u"", u"end", idno, text = idno)
            self.treeview.set(idno, u"URL", row[1])
            
        self.treeview.config(height = idno, selectmode = u"browse")
        ttk.Button(self.frame, text = u"Open", command = self.displayPage).pack(pady = 5)
        
    def displayPage(self):
        item = self.treeview.selection()
        getPath = self.treeview.set(item).get(u"URL")
        url = os.path.basename(getPath)
        self.label2.set(url)
        file = open(getPath, u"r")
        content = file.read()
        file.close()
        self.text.config(state = NORMAL)
        self.text.delete(u"1.0", u"end")
        self.text.insert(u"1.0", content)
        self.text.edit_modified(False)
        self.storedPages.destroy()
        
    def loadPage(self):
        url = self.label2.get()
        if url == u"":
            messagebox.showerror(u"Error", u"Create a new file or open an existing one.")
        elif url == u"UNTITLED":
            self.saveAsPage()
        elif self.text.edit_modified() == True:
            saveOK = messagebox.askokcancel(u"Save File before Loading",
                    u"Would you like to save this file?")
            if saveOK == True:
                content = self.text.get(u"1.0", u"end")
                fullPath = os.path.realpath(url)
                file = open(fullPath, u"w")
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

if __name__ == u"__main__":main()

        
            
