@echo off
:start
title Fuckifier -- by Text2Hex
echo Fuckifier by Text2Hex
start "..\Fuckifier Executables\Fuckifier.exe"

:checkfort2hfuckifier
if not exist "..\Fuckifier Executables\Fuckifier.exe" (
     echo You deleted Fuckifier, or your anti-virus flagged it. Please reinstall.
     pause
     exit /b

:exit
exit /b
