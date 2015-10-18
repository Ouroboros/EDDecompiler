@echo off
cd/d "%~dp0"

rem c0130.bin.py
rem fachr176._bn.py
rem t_name.py

::for %%i in (as*.py) do %%i
::for %%i in (ms*.py) do %%i
for %%i in (sysatk*.py) do %%i

move /y *._bn D:\Game\Falcom\ED_AO\patch\system
move /y *._dt D:\Game\Falcom\ED_AO\patch\text
move /y *.bin D:\Game\Falcom\ED_AO\patch\scena
move /y *.dat D:\Game\Falcom\ED_AO\patch\battle\dat
move /y sysatk*.eff D:\Game\Falcom\ED_AO\patch\effect\eff

start D:\Game\Falcom\ED_AO\ED_AO_CRACK.exe


call ..\cleanup.bat
