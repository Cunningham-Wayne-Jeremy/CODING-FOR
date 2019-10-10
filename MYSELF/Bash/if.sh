echo "Can you guess the number I am thinking of?"
echo "Enter a number between 1 and 5"
read GUESS
if [ $GUESS -eq 3 ]
  then
  echo "You Guessed the Correct Number!"
else
 echo "Try again!"
fi
