### File Transfer GUI and Database

This program allows a user to copy files from one folder to another and record the date and time this is being done.

I created a graphical user interface using the wxPython module that allows a user to select a desktop folder and identify the files that were either created or modified within the last 24 hours. The user can then copy those files to another folder at the click of a button. I used the shutil module in Python to copy the files.

As the files are to be copied over manually every 24 hours, I used the sqlite module to create a database that would store the date and time of each file check. This information would then be displayed on the UI and updated with each file check to let users know if they need to perform another check.

I wrote the code for this program in Python 2.7 and Python 3.4.
