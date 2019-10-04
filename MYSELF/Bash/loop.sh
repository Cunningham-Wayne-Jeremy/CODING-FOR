#Loop through the name of each server and print it out to stfd out
SERVERNAMES=("us-east01" "us-west01" "us-north01" "us-south01")
COUNT=0
for i in ${SERVERNAMES[*]}; do
 echo "Processing Server: ${SERVERNAMES[COUNT]}"
 COUNT="`expr $COUNT + 1`"
done

 
