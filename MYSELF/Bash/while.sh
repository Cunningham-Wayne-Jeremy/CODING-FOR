#!/bin/bash
echo "Enter a number"
read NUMBER

COUNT=1

while [ $COUNT -le $NUMBER ];do
 echo "Hello World -$COUNT"
 COUNT=`expr $COUNT + 1`
done
