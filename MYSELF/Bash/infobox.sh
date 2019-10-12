#!/bin/bash 

#variable declaration
INFOBOX=${INFOBOX=dialog} 
TITLE="Default"
MESSAGE="Welcome Message"
XCOORD=10
YCOORD=20

#display box function
funcDisplayInfoBox () {
	$INFOBOX --title "$1" --infobox "$2" "$3" "$4"
	sleep "$5"
}


COMMAND="$1"

#check for missing arguments
[ -z "$COMMAND" ] && { echo "NO COMMAND PASSED"; exit 1; }

case "$COMMAND" in
	ilovesophie)
		funcDisplayInfoBox "WARNING!" "Dadda loves Sophie too much..." "11" "21" "5"
		echo "Spanking her tush"
		;;
	ilovemomma)
		funcDisplayInfoBox "WARNING!" "Dadda loves Momma too much..." "11" "21" "5" 
		echo "Spanking mommas tush"
		;;
	*)
		funcDisplayInfoBox "Information" "You are not doing anything fun!" "11" "21" "5"
		echo "Not doing anything.."
		;;
esac
