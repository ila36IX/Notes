#!/usr/bin/env bash

#################################################################
########################## HOW TO USE ###########################
#################################################################
# Your file that consists of chuncks linkes should be named input
# and put in the somae directory as this script
#################################################################

function trap_ctrlc ()
{
	# perform cleanup here
	echo "You've canceled the scirpt"
	echo "Surly you have you're reasons ✌️"
	rm .*.ts
	exit 2
}

trap "trap_ctrlc" 2

python3 .download_from_clubhouse.py 2>/dev/null

ls -1v .*.ts | while read line
do
	cat $line >> output.ts
done

rm .*.ts

echo "Your file is under the name input.ts, have fun!"
echo "\nDone ✅"
