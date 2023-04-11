### Settings
import os
from modules.scripts.startmcservice import *
user = os.getlogin()
jarlink = 'https://api.papermc.io/v2/projects/paper/versions/1.19.4/builds/504/downloads/paper-1.19.4-504.jar' # Link to the paper version that will be used
jarversion = 'paper-1.19.4-504.jar' # Jar version, write exact name
homedirectory = str('/home/%s' % user)
dependencies = ['git', 'github-cli']
ram = str(2) # Ram to be used, in GB
mcserviceconfig = str(serviceinfo % (ram, ram, jarversion))
#ghserverurl = str() # Gh repo for server