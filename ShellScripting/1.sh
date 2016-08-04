#!/bin/bash

echo "Date and Time :" >> assignment.log
date '+%c' >> assignment.log 

echo "Hostname :" >> assignment.log
hostname >> assignment.log

echo "Type and version on operating system :" >> assignment.log
uname -ov >> assignment.log

echo "Absolute path of Home directory :" >> assignment.log
echo $HOME >> assignment.log

echo "List of users currently logged in :" >> assignment.log
who -u >> assignment.log

echo "List of groups current user belongs to :" >> assignment.log
groups >> assignment.log

echo "List of all files (excluding directory)" >> assignment.log
find . -not -type d >> assignment.log