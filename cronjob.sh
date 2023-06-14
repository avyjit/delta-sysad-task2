#!/bin/env bash

cron_expression="10 10 3-31/3 5,6,8 0 $(pwd)/backupdb.sh"
temp=$(mktemp)
crontab -l > $temp
echo "$cron_expression" >> $temp
crontab $temp
rm $temp
echo "Backup cronjob has been added..."