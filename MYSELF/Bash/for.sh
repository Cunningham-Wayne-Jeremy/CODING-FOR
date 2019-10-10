#!/bin/bash

SHELL="`ls *.sh`"

for SCRIPT in $SHELL;do
 DISPLAY="`cat $SCRIPT`"
 echo "File:$SCRIPT - CONTENTS $DISPLAY"
done
