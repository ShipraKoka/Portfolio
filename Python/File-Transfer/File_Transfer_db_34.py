import wx
import os
import shutil
from datetime import datetime, timedelta
import sqlite3

userHome = os.path.expanduser('~')
userPath = userHome + "\Desktop"
conn = sqlite3.connect("CustomerOrders.db")
c = conn.cursor()


def createTable():
    c.execute("CREATE TABLE if not exists File_Check(\
        DATETIME NOT NULL);")

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None,\
            title = title, size = (400, 300))
        panel = wx.Panel(self)
        
        wx.StaticBox(panel, label = "Customer Orders File Transfer",\
                     pos = (10, 10), size = (360, 240))

        #Choose Source folder button
        chooseSource = wx.Button(panel, label = "Choose a source folder", pos = (20, 50))
        chooseSource.Bind(wx.EVT_BUTTON, self.chooseSourceFolder)

        # Choose Destination folder button
        chooseDest = wx.Button(panel, label = "Choose a destination folder", pos = (20, 110))
        chooseDest.Bind(wx.EVT_BUTTON, self.chooseDestFolder)

        self.sourceFolder = wx.TextCtrl(panel, size = (300, -1), pos = (25, 80))
        self.destFolder = wx.TextCtrl(panel, size = (300, -1), pos = (25, 140))
        
        #Button to transfer files
        copyFiles = wx.Button(panel, label = "Copy Files", pos = (150, 180))
        copyFiles.Bind(wx.EVT_BUTTON, self.copyCustOrders)

        #Label to display last file check
        self.lastFileCheck = wx.StaticText(panel, label = "", pos = (20, 220))
        self.getLastDateTime()

    def getLastDateTime(self):
        global lastCheck, maxTime, lastCheckStr
        c.execute("SELECT MAX(DATETIME) from File_Check;")
        maxTime = c.fetchone()
        if maxTime[0] is None:
            return
        else:
            lastTime = str(maxTime[0])
            lastCheck = datetime.strptime(lastTime, "%Y-%m-%d %H:%M:%S.%f")
            lastCheckStr = lastCheck.strftime("%B %d, %Y at %I:%M %p")
            self.lastFileCheck.SetLabel("The last file check was done on {}.".format(lastCheckStr))
        
    def chooseSourceFolder(self, event):
        dialog = wx.DirDialog(self, "Choose a Source folder", defaultPath = userPath)
        if dialog.ShowModal() == wx.ID_OK:
            self.sourceFolder.SetValue(dialog.GetPath())
        dialog.Destroy()
        
    def chooseDestFolder(self, event):
        dialog = wx.DirDialog(self, "Choose a Destination folder", defaultPath = userPath)
        if dialog.ShowModal() == wx.ID_OK:
            self.destFolder.SetValue(dialog.GetPath())
        dialog.Destroy()

    def copyCustOrders(self, event):
        global current
        sourcePath = self.sourceFolder.GetValue()
        destPath = self.destFolder.GetValue()
        allFiles = os.listdir(sourcePath)
        for textFile in allFiles:
            #get time the file was created
            created = os.path.getctime(os.path.join(sourcePath, textFile))
            dateCreated = datetime.fromtimestamp(created)
            
            #get time the file was modified
            modified = os.path.getmtime(os.path.join(sourcePath, textFile))
            dateModified = datetime.fromtimestamp(modified)

            if maxTime[0] is None:
                #copy files created/edited within the last 24 hours
                last24hours = datetime.now() - timedelta(hours=24)
                if dateCreated > last24hours or dateModified > last24hours:
                    shutil.copy(os.path.join(sourcePath, textFile), destPath)
            else:
                #copy files created/edited since last file check
                if dateCreated > lastCheck or dateModified > lastCheck:
                    shutil.copy(os.path.join(sourcePath, textFile), destPath)

        #update database
        current = datetime.now()
        now = str(current)
        sql_insert = "INSERT INTO File_Check VALUES('{}');".format(now)
        c.execute(sql_insert)
        conn.commit()
        currentFileCheck = current.strftime("%B %d, %Y  %I:%M %p")
        self.lastFileCheck.SetLabel("The last file check was done on {}.".format(currentFileCheck))

        if maxTime[0] is None:
            wx.MessageBox("Customer orders created or edited within the last\n"
                      "24 hours have been copied for transfer to the home office.",\
                      "Transfer Completed", wx.OK)
        else:
            wx.MessageBox("Customer orders created or edited since {}\n"
                    "have been copied for transfer to the home office.".format(lastCheckStr),\
                    "Transfer Completed", wx.OK)

        self.sourceFolder.Clear()
        self.destFolder.Clear()

createTable()

app = wx.App()
frame = Frame("File Transfer")
frame.Show()
app.MainLoop()



