#!/bin/bash
echo "Enter a number between 1 and 3"
read NUMBER
if [ "$NUMBER" -eq "3" ]
then
 echo "You have entered number $NUMBER"
elif [ "$NUMBER" -eq "2" ]
then
 echo "You have entered number $NUMBER"
elif [ "$NUMBER" -eq "1" ]
then
 echo "You have entered number $NUMBER"
else
 echo "YOU DIDNT FOLLOW THE INSTRUCTIONS!"
fi
