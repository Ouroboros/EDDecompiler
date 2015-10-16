@echo off

cd/d "%~dp0"

set input=J:\Falcom\ED_AO\data\scena
rem set input=J:\PSP\Eiyuu_Densetsu_Ao_no_Kiseki\USRDIR\data\scena

del /q %input%\*.py

ScenarioScript.py %input%\

call cleanup.bat
