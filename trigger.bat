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
echo (1) twitter CLI

echo.

set /p caso=elige opcion: 

echo.
if %caso%==1 goto TWEET

echo.
echo.

:TWEET
python C:\Users\exp\scripts\scraping\plantillas\twitter\twitterlineadecomando.py -h
echo.
set /p opcion=elige opcion: 
python C:\Users\exp\scripts\scraping\plantillas\twitter\twitterlineadecomando.py %opcion%
goto RETURN

