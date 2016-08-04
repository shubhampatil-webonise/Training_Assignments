#!/bin/bash

echo "Files before renaming :"
ls *.txt
rename -n 's/^/rename/' *.txt
echo "Files are renaming :"
ls *.txt


