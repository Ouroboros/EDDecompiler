@echo off

cd/d "%~dp0"

set "input=D:\Game\Steam\steamapps\common\Trails in the Sky FC\ED6_DT01"
rem set input=J:\PSP\Eiyuu_Densetsu_Ao_no_Kiseki\USRDIR\data\scena

del /q "%input%\*.py"

ED6FCScenarioScript.py "%input%"
