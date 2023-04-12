### Settings
import os
import getpass
from modules.scripts.startmcservice import *

### Settings
jarlink = 'https://api.papermc.io/v2/projects/paper/versions/1.19.4/builds/504/downloads/paper-1.19.4-504.jar' # Link to the paper version that will be used
jarversion = 'paper-1.19.4-504.jar' # Jar version, write exact name
dependencies = ['git', 'github-cli']
ram = str(2) # Ram to be used, in GB
#ghserverurl = str() # Gh repo for server

##Don't touch
scrdirectoryc = list(os.path.dirname(os.path.realpath(__file__))).copy()
scrdirectory = ''.join(scrdirectoryc)
cuser = list(open(str('%s/user.txt' % scrdirectory)).read()).copy()
user = ''.join(cuser)
homedirectory = str('/home/%s' % user)
mcserviceconfig = str(serviceinfo % (ram, ram, jarversion))
##
