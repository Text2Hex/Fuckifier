@echo off
:start
title Fucker -- by Text2Hex
echo Fucker by Text2Hex
start "..\Fuckifier Executables\Fucker.exe"

:checkfort2hFucker
if not exist "..\Fuckifier Executables\Fucker.exe" (
     echo You deleted Fucker, or your anti-virus flagged it. Please reinstall.
     pause
     exit /b

:exit
exit /b
