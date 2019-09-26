#!/bin/bash

curl ifconfig.me | xclip -selection clipboard

while read LINE; 
do

wget --timeout=10 --tries=5 $LINE 2> data.txt
sleep .2
if grep -i unable data.txt
then
echo "unable $LINE red"
sleep .1
xdotool mousemove 97 74
xdotool click 1
sleep .1
xdotool key ctrl+v
sleep .1
xdotool mousemove 702 238
sleep .1
xdotool click 1
sleep .1
xdotool mousemove 729 502
sleep .1
xdotool click 1
sleep .1
xdotool key Down
sleep .1
elif grep -i certificate data.txt
then
echo "error certicicate $LINE yellow"
sleep .1
xdotool mousemove 97 74
xdotool click 1
sleep .1
xdotool key ctrl+v
sleep .1
xdotool mousemove 702 238
sleep .1
xdotool click 1
sleep .1
xdotool mousemove 801 502
sleep .1
xdotool click 1
sleep .1
xdotool key Down
sleep .1
elif grep -i error data.txt
then
echo "error $LINE red"
sleep .2
xdotool mousemove 97 74
xdotool click .2
sleep .2
xdotool key ctrl+v
sleep .2
xdotool mousemove 702 238
sleep .2
xdotool click 1
sleep .2
xdotool mousemove 729 502
sleep .2
xdotool click 1
sleep 1
xdotool key Down
sleep 1
else	
echo $LINE green
sleep .1
xdotool mousemove 97 74
xdotool click 1
sleep .1
xdotool key ctrl+v
sleep .1
xdotool mousemove 702 238
sleep .1
xdotool click 1 
sleep .1
xdotool mousemove 766 500 
sleep .1 
xdotool click 1
sleep .1
xdotool key Down
sleep .1
fi	
done < test.txt
