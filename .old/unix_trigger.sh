#!/bin/sh
#python version must be python 3.x (tested on 3.8 and above)
/usr/bin/python twitter.py -h
echo ''
printf "elige opcion: " && read -r opcion
/usr/bin/python twitter.py $opcion
