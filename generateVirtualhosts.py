import os
import shutil

hosts = "C:\\Windows\\System32\\drivers\\etc\\hosts"
httpd = "C:\\apps\\httpd\\apache\\conf\\httpd.conf"
vhosts = "C:\\apps\\httpd\\apache\\conf\\extra\\httpd-vhosts.conf"

vhostsTime = os.path.getmtime(vhosts)

def writeVirtualhost(filename):
    with open(hosts, "a") as myfile:
        myfile.write("\n::1             "+filename+".loc")

    with open(httpd, "a") as myfile:
        myfile.write("\n<Directory \"E:/projects/"+filename+"\">")
        myfile.write("\nOptions Indexes FollowSymLinks Includes ExecCGI")
        myfile.write("\nAllowOverride All")
        myfile.write("\nRequire all granted")
        myfile.write("\n</Directory>")

    with open(vhosts, "a") as myfile:
        myfile.write("\n<VirtualHost *:80>")
        myfile.write("\nServerAdmin postmaster@dummy-host.localhost")
        myfile.write("\nDocumentRoot \"E:/projects/"+filename+"\"")
        myfile.write("\nServerName "+filename+".loc")
        myfile.write("\nServerAlias www."+filename+".loc")
        myfile.write("\n</VirtualHost>")

shutil.copy2(hosts, hosts+'.bak')
shutil.copy2(httpd, httpd+'.bak')
shutil.copy2(vhosts, vhosts+'.bak')

for filename in os.listdir('.'):
    folderTime = os.path.getctime(filename)
    if os.path.isdir(filename) == True:
          if (folderTime > vhostsTime):
              writeVirtualhost(filename)
              print(filename)


