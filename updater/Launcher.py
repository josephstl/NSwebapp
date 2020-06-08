import easygui, subprocess, os, sys, webbrowser
from ftplib import FTP
# ftp server properties
ftpDomain = "10.1.1.147"
usrName = "anonymous"
pssWord = ""
# this looks at the current folder and finds the first file
# which is why verson files start with '$'
currDir = os.getcwd()
lcDir = os.listdir(currDir)
version = lcDir[0]
versionCheck = False
#this downloads files from ftp
def grabfile(filename):
    localfile = open(filename, 'wb')
    #ftp.retrbinary('RETR ' + filename, localfile.write, 4096)
    ftp.retrbinary('RETR ' + filename, localfile.write)
    localfile.close()
# This connects to the ftp server using the pre establised properties
ftp = FTP(ftpDomain)
ftp.login(user=usrName, passwd=pssWord)
file_list = []
file_list = ftp.nlst()
# this finds the verson file on the server and compares it
print(file_list[0])
if file_list[0] == version:
    versionCheck = True
#this call the webapp executable if the version is correct
# if the version is different then renames the current executable as backup
# downloads the new version file and executable
# then double checks for the executable, if the download failed it reverts
# to the older version
if versionCheck :
    subprocess.call("WebApp.exe")
else:
    if os.path.exists(currDir + "\\PastWebApp.exe") and os.path.exists(currDir + "\\WebApp.exe"):
        os.remove(currDir + "\\PastWebApp.exe")
    os.rename(currDir + r'\WebApp.exe', currDir + r'\PastWebApp.exe')
    os.remove(currDir + '\\'+version)
    print("downloading version :" + file_list[0])
    grabfile(file_list[0])
    print("downloading Web App")
    grabfile("WebApp.exe")
    print("done ! :)" )
    if os.path.exists(currDir + "\\WebApp.exe"):
        subprocess.call("WebApp.exe")
    else:
        os.rename(currDir + r'\PastWebApp.exe', currDir + r'\WebApp.exe')
        subprocess.call("WebApp.exe")
sys.exit()
