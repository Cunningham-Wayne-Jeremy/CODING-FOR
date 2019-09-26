#!/bin/bash
echo "Enter a username"

#read inputfromuser
ifcorrect='false'
while true;
do
read inputfromuser
if echo $inputfromuser | grep -Eq 'p[-0-9]{7}$'
then 
echo "You did good"
break 
else echo "Try again"
fi
done
