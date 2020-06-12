#!/bin/bash

##########################################################
# Creates/ Saves csv file to the OSINT_Reports Directory #
##########################################################

DATE=`date "+%Y-%m-%d_%H-%M-%S"`

mkdir -p "/home/osint/Desktop/OSINT_REPORTS/"
mkdir -p "/home/osint/Desktop/OSINT_REPORTS/Report_$DATE"

FILENAME="/home/osint/Desktop/OSINT_REPORTS/Report_$DATE/Report_$DATE.csv"
FILENAME_HASH="/home/osint/Desktop/OSINT_REPORTS/Report_$DATE/Report_Hash.txt"

printf "Name\tPath\tDate_Analyzed\tMD5_Hash\n" >> $FILENAME
echo "Generating Report_$DATE.csv..."

############################################################
###  Reads all the files of the OSINT_OUTPUT Directory  ####
############################################################

OUTPUT_DIR="/home/osint/Desktop/OSINT_OUTPUT/"

readarray -d '' array < <(find $OUTPUT_DIR -name "*.*" -print0)
for element in "${array[@]}"; 
do
FILE_NAME=${element##*/}

FILE_DATE=$((ls -la "$element")|awk '{print $6,$7,$8}')

FILE_HASH=$(md5sum "$element"| awk '{print $1}')

printf "$FILE_NAME\t$element\t$FILE_DATE\t$FILE_HASH\n" >> $FILENAME
#echo "$FILE_NAME | $element | $FILE_DATE | $FILE_HASH"
#echo "---------------------------------"
done


##############################################################
###       Saves Report Name and Hash to .txt File          ###
##############################################################

REPORT_HASH=$(md5sum "$FILENAME"| awk '{print $1}')
REPORT_NAME="${FILENAME##*/}"

printf "Report Name: $REPORT_NAME\n" >> $FILENAME_HASH
printf "Report Hash: $REPORT_HASH" >> $FILENAME_HASH

echo "$REPORT_NAME has been generated!"