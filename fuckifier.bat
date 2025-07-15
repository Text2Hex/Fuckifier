@echo off
setlocal

title Fuckifier Launcher
color 0a

echo.
echo Choose 1 or 2:
echo 1 - Opens Fuckifier [customTkinter]
echo 2 - Opens Fucker [Tkinter]
echo 3 - Opens Fuckifier [customTkinter] with a debug console
echo 4 - Opens Fucker [Tkinter] with a debug console
set /p follow=

if "%follow%"=="1" (
    start "" "Launcher\fuckifier.bat"
)

if "%follow%"=="2" (
    start "" "Launcher\fucker.bat"
)

if "%follow%"=="3" (
    python "ShittyFiles\Fuckifier\fuckifier.py"
)

if "%follow%"=="4" (
    python "ShittyFiles\Fuckifier\fucker.py"
)

:end
endlocal
