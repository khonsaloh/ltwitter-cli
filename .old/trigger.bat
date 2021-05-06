@echo off
color d
title login
::doskey alias=doskey /MACROS
:RETURN
echo.
echo.
echo =============== TWITTER =====================
echo.

python twitter.py -h
echo.
set /p opcion=elige opcion: 
python twitter.py %opcion%
goto RETURN

