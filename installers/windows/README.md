## To create an installer for Windows:
- On the laptop, goto the GitHub\marxan-server and marxan-client folders and run git pull to get the latest versions (or use GitHub Desktop)
- Make sure all of the following files are in the GitHub\marxan-web\installers\windows folder:
 dump.sql
 marxan.ico
 marxan-web-windows.nsi
 Miniconda2-latest-Windows-x86_64.exe
 postgis-bundle-pg10x64-setup-2.5.1-1.exe
 postgresql-10.7-1-windows-x64.exe  
 
- Open the *.nsi file from GitHub on the laptop
- Update the output version, e.g. marxan-web-v0.6.6.exe 
- Make the *.exe file and upload into an existing release or as a new release in the marxan-web repo

