@echo off
color d
title login
::doskey twitter=C:\Users\exp\Desktop\scripts\VisualBasicScripts\twitter.vbs
::doskey alias=doskey /MACROS
:RETURN
echo.
echo.
echo =============== TWITTER =====================
echo.

python C:\Users\exp\scripts\scraping\plantillas\twitter\twitterlineadecomando.py -h
echo.
set /p opcion=elige opcion: 
python C:\Users\exp\scripts\scraping\plantillas\twitter\twitterlineadecomando.py %opcion%
goto RETURN

