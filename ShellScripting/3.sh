#!/bin/bash

echo "Files before renaming (with .txt extension) :"
ls
echo "Date and time when files (with.txt extension) were renamed :" >> assignment2.log
date '+%c' >> assignment2.log
rename -v 's/^/rename/' *.txt
echo "Listing of directory :" >> assignment2.log
ls >> assignment2.log
echo "Files after renaming (with .txt extension) :"
ls



echo "Files before renaming (starting with x) :"
ls
echo "Date and time when files (starting with x) were renamed :" >> assignment2.log
date '+%c' >> assignment2.log
rename -v 's/^/rename/' x*
echo "Listing of directory :" >> assignment2.log
ls >> assignment2.log
echo "Files after remaining (starting with x) :"
ls