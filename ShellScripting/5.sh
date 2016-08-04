#!/bin/bash

for file in $(ls -p| grep -v / | head -4)
do 
mv $file public_html
done
