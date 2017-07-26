#!/bin/bash

f=/share/export_file.txt
b='##########          '
a='          ##########'

rm $f
touch $f

for i in $( ls ); do
	echo $b$i$a >> $f 
	cat $i >> $f
done

