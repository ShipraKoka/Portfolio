import shutil
import os
from datetime import datetime, timedelta

userHome = os.path.expanduser('~')
source = userHome + "\Desktop\Orders"
allFiles = os.listdir(source)
destination = userHome + "\Desktop\Processed"

def copyCustOrders():
    for textFile in allFiles:
        #get time the file was created
        created = os.path.getctime(os.path.join(source, textFile))
        dateCreated = datetime.fromtimestamp(created)
        
        #get time the file was modified
        modified = os.path.getmtime(os.path.join(source, textFile))
        dateModified = datetime.fromtimestamp(modified)
        last24hours = datetime.now() - timedelta(hours=24)
        
        #copy files created/edited within the last 24 hours
        if dateCreated > last24hours or dateModified > last24hours:
            shutil.copy(os.path.join(source, textFile), destination)
            
    print "All customer orders created or edited within the last 24 hours \
have been copied for transfer to the home office."

copyCustOrders()
