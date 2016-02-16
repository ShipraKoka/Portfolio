import wx
import shutil
import os
from datetime import datetime, timedelta

userHome = os.path.expanduser('~')
userPath = userHome + "\Desktop"

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
        copyFiles = wx.Button(panel, label = "Copy Files", pos = (150, 200))
        copyFiles.Bind(wx.EVT_BUTTON, self.copyCustOrders)

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
            
            last24hours = datetime.now() - timedelta(hours=24)
            
            #copy files created/edited within the last 24 hours
            if dateCreated > last24hours or dateModified > last24hours:
                shutil.copy(os.path.join(sourcePath, textFile), destPath)

        wx.MessageBox("Customer orders created or edited within the last\n"
                      "24 hours have been copied for transfer to the home office.",\
                      "Transfer Completed", wx.OK)

        self.sourceFolder.Clear()
        self.destFolder.Clear()

app = wx.App()
frame = Frame("File Transfer")
frame.Show()
app.MainLoop()

