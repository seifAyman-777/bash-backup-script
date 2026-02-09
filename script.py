#!/bin/bash

# variables

source_dir="/root/backup"
log_file="backup.log"
remote_host="root@192.168.64.4"
remote_dir="/root/"

#functiin to preform the backup

perform-backup() {
       rsync -avz "$source_dir" "$remote_host":"$remote_dir" > "$log_file" 2>&1
       if [ $? -eq 0 ]
       then 
                 eche "Backup successful: $(date)" >> "$log_file"
       else 
                 echo "Backup faild: $(date)" >> "$log_file"
       fi
}

perform-backup





