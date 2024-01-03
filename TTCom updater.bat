@ECHO OFF
:choice
set /P c=Would you like to update to the latest version of TTCom[Y/N, or b for the latest beta revision]?
if /I "%c%" EQU "Y" goto :yes
if /I "%c%" EQU "N" goto :no
if /I "%c%" EQU "B" goto :beta
goto :choice
:yes
echo "Updateing, please wait."
taskkill /f /im ttcom.exe
rm -r iniparse
rm -r mplib
del bitflags.py
del conf.py
del LICENSE.txt
del parmline.py
del trigger_cc.py
del triggers.py
del tt_attrdict.py
del ttapi.py
del ttcom.exe
del ttcom.htm
del ttcom.py
del TTComCmd.py
del ttflags.py
echo "Downloading, please wait.
curl -C - -LO https://www.dlee.org/teamtalk/ttcom/ttcom.zip
echo "Extracting, please wait."
7z -y  x ttcom.zip
echo "Deleting unnecessary files, please wait."
del ttcom.zip
del ttcom_default.conf
exit
:beta
echo "Updateing, please wait."
taskkill /f /im ttcom.exe
rm -r iniparse
rm -r mplib
del bitflags.py
del conf.py
del LICENSE.txt
del parmline.py
del trigger_cc.py
del triggers.py
del tt_attrdict.py
del ttapi.py
del ttcom.exe
del ttcom.htm
del ttcom.py
del TTComCmd.py
del ttflags.py
echo "Downloading latest beta revision, please wait.
curl -C - -LO https://www.dlee.org/teamtalk/ttcom/beta/ttcom.zip
echo "Extracting, please wait."
7z -y  x ttcom.zip
echo "Deleting unnecessary files, please wait."
del ttcom.zip
del ttcom_default.conf
exit
:no
echo "TTCom will not be updated at this time."
pause
exit