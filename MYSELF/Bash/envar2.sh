MYUSERNAME="username"
declare MYPASSWORD="YOUWISH"
STARTOFSCRIPT=`date`
sleep 10
ENDOFSCRIPT=`date`
echo "Your user name is $MYUSERNAME"
echo Your password is $MYPASSWORD
echo "The script began at $STARTOFSCRIPT"
echo The script stoped at $ENDOFSCRIPT
echo "=================================================="
echo "=================================================="
TODAYSDATE="`date`"
echo $TODAYSDATE 
USERFILES="`find run ~ jercun`"
echo $USERFILES

