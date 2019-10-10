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
	shutdown)
		funcDisplayInfoBox "WARNING!" "We are SHUTTING DOWN the System..." "11" "21" "5"
		echo "Shutting Down!"
		;;
	restart)
		funcDisplayInfoBox "WARNING!" "We are RESTARTING the System..." "11" "21" "5" 
		echo "Restarting System!"
		;;
	*)
		funcDisplayInfoBox "Information" "You are not doing anything fun!" "11" "21" "5"
		echo "Not doing anything.."
		;;
esac
