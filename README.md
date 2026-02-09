# Automated Backup Script

This project is a Bash script that performs automated backups using `rsync`
from a local directory to a remote Linux server over SSH.

## Features
- Secure backup over SSH
- Uses rsync for efficient file transfer
- Logs success and failure events
- Simple and lightweight Bash script

## Requirements
- Linux system
- Bash
- rsync installed
- SSH access to the remote server

## Configuration
Edit the following variables in `backup.sh`:

```bash
source_dir="/root/backup"
remote_host="root@192.168.64.4"
remote_dir="/root/"
log_file="backup.log"

