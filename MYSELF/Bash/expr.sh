#!/bin/bash
#echo "`expr 3-4\*23\/123434-\(433+453324234/)`"
#The above code fails..... WHY? SPACING. Each character must be a space apart...
#Lets try again
set -e #shows errors
#echo "`expr 3 - 4 \* 23 / 123434 - \( 433 + 453324234 /)`"
#The above code doesnt work and after examining it ALOT I finally found that the last ) has a forward slash instead of a \
echo "`expr 3 - 4 \* 23 / 123434 - \( 433 + 453324234 \)`"
