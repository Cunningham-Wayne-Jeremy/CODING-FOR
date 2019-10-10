#!/bin/bash
echo "ENTER FILE NAME"
read FILE

while read -r SUPERHERO;do
 echo "Superhero Name:$SUPERHERO"
done < "$FILE"
