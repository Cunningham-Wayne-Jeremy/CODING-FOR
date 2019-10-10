#!/bin/bash

# demo of reading and writing to a file using a file descriptor

echo "Enter a file name to read: "

read FILE
#Writes to the file
exec 5<>$FILE

while read -r SUPERHERO; do

  echo "Superhero Name: $SUPERHERO"
#Done writing to the file
done <&5

echo "File Was Read On: `date`" >&5

exec 5>&-
