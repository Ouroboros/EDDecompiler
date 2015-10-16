@echo off

cd/d "%~dp0"

del /q J:\Falcom\ED_AO\data\battle\dat\ms*.py

BattleMonsterStatus.py J:\Falcom\ED_AO\data\battle\dat\

call cleanup.bat
